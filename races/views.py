# Import Django's built-in functions for web views
from django.shortcuts import render, get_object_or_404, redirect
# Import decorator that requires user to be logged in
from django.contrib.auth.decorators import login_required
# Import Django's message system for success/error notifications
from django.contrib import messages
# Import Django's pagination system to split long lists into pages
from django.core.paginator import Paginator
# Import our Race and Comment models from the current app
from .models import Race, Comment, AccountDeletionRequest
# Import our custom forms
from .forms import RaceForm


def race_list(request):
    """
    VIEW 1: Homepage - Display races based on user permissions
    
    This view shows different races depending on who's viewing:
    - Everyone: approved and published races only
    - Admin: all races (approved and pending approval)  
    - Race creators: their own races + approved races by others
    
    Also handles difficulty filtering via URL parameter
    """
    
    # STEP 1: Get base queryset of published races
    if request.user.is_authenticated and (request.user.is_staff or request.user.is_superuser):
        # ADMIN VIEW: Show all published races (approved + pending approval)
        races = Race.objects.filter(status=1).order_by('race_date')
    else:
        # PUBLIC VIEW: Only show approved and published races
        # For logged-in users, also include their own unapproved races
        if request.user.is_authenticated:
            from django.db.models import Q
            # Show: (approved races) OR (user's own races)
            races = Race.objects.filter(
                Q(status=1, approved=True) | 
                Q(status=1, created_by=request.user)
            ).order_by('race_date')
        else:
            # Anonymous users: only approved races
            races = Race.objects.filter(status=1, approved=True).order_by('race_date')
    
    # STEP 1.5: Apply difficulty filter if provided
    difficulty_filter = request.GET.get('difficulty')
    if difficulty_filter and difficulty_filter != 'ALL':
        races = races.filter(difficulty=difficulty_filter)
    
    # STEP 2: Split races into pages (pagination)
    # This prevents showing 100+ races on one page
    # CHANGE THIS NUMBER to control races per page:
    # 6 = 6 races per page | 9 = 9 races per page | 12 = 12 races per page
    paginator = Paginator(races, 6)  # Show 6 races per page (2 rows of 3)
    
    # STEP 3: Get which page number user wants to see
    # If URL is "/?page=2", this gets "2"
    # If no page specified, defaults to page 1
    page_number = request.GET.get('page')
    
    # STEP 4: Get the actual races for this page
    # If page=2 and we show 5 per page, this gets races 6-10
    page_obj = paginator.get_page(page_number)
    
    # STEP 5: Prepare data to send to template
    context = {
        'races': page_obj,  # The races to display on this page
        'is_paginated': page_obj.has_other_pages(),  # True if more than 1 page
        'page_obj': page_obj,  # Pagination info (current page, total pages, etc.)
        'difficulty_choices': Race.DIFFICULTY_CHOICES,  # Available difficulty filters
        'current_difficulty': difficulty_filter or 'ALL',  # Currently selected filter
    }
    
    # STEP 6: Render the HTML template with our data
    # Django finds 'races/race_list.html' template and fills it with context data
    return render(request, 'races/race_list.html', context)


def race_detail(request, pk):
    """
    VIEW 2: Race Detail Page - Show race with comments
    
    Handles both displaying race details AND processing new comments
    """
    
    # STEP 1: Get the race from database (published races only)
    race = get_object_or_404(Race, pk=pk, status=1)
    
    # STEP 2: Check if user has permission to view this race
    if not race.is_visible_to_user(request.user):
        from django.http import Http404
        raise Http404("Race not found or not available.")
    
    # STEP 3: Get comments for this race
    comments = race.comments.filter(approved=True).order_by('-created_on')
    comment_count = comments.count()
    
    # STEP 4: Handle comment submission
    if request.method == "POST" and request.user.is_authenticated:
        comment_body = request.POST.get('body')
        if comment_body:
            Comment.objects.create(
                race=race,
                author=request.user,
                body=comment_body
            )
            messages.success(request, 'Your comment has been added!')
            return redirect('race-detail', pk=race.pk)
    
    # STEP 5: Send race and comments data to template
    context = {
        'race': race,
        'comments': comments,
        'comment_count': comment_count,
    }
    return render(request, 'races/race_detail.html', context)


@login_required  # This decorator ensures only logged-in users can access this view
def create_race(request):
    """
    VIEW 3: Create New Race - Form for users to add new races
    
    This view shows a form where logged-in users can create new races.
    It handles both showing the empty form AND processing the submitted data.
    """
    
    # STEP 1: Check if user is submitting form data (POST) or just viewing form (GET)
    if request.method == 'POST':
        # USER SUBMITTED THE FORM - Process the data
        
        # STEP 2: Create form instance with submitted data
        # request.POST = text data (name, description, etc.)
        # request.FILES = uploaded files (race image)
        form = RaceForm(request.POST, request.FILES)
        
        # STEP 3: Check if all form data is valid
        if form.is_valid():
            # STEP 4: Create race object but don't save to database yet
            # commit=False means "create object in memory but don't save"
            race = form.save(commit=False)
            
            # STEP 5: Add the current user as the race creator
            race.created_by = request.user
            
            # STEP 6: Set race status to "Published" but not yet approved
            race.status = 1  # Published (not draft)
            race.approved = False  # Needs admin approval
            
            # STEP 7: Now save the complete race to database
            race.save()
            
            # STEP 8: Show appropriate success message
            if request.user.is_staff or request.user.is_superuser:
                messages.success(request, f'Race "{race.name}" created and published!')
            else:
                messages.success(
                    request, 
                    f'Race "{race.name}" created! It will be visible to others once approved by admin.'
                )
            
            # STEP 9: Redirect user to the new race's detail page
            return redirect('race-detail', pk=race.pk)
    
    else:
        # USER IS JUST VIEWING THE PAGE - Show empty form
        form = RaceForm()
    
    # STEP 10: Show the create race form (empty or with errors)
    return render(request, 'races/create_race.html', {'form': form})


@login_required  # Only logged-in users can see their own races
def my_races(request):
    """
    VIEW 4: My Races - Show races created by the current logged-in user
    
    This view shows only the races that the current user has created.
    It's like a personal dashboard for managing your own races.
    """
    
    # STEP 1: Get only races created by the current user
    # filter(created_by=request.user) = only races where creator is current user
    # order_by('-created_at') = newest races first (- means descending order)
    races = Race.objects.filter(created_by=request.user).order_by('-created_at')
    
    # STEP 2: Split user's races into pages
    # Show 6 races per page (smaller number since it's personal view)
    paginator = Paginator(races, 6)  # Show 6 races per page (2 rows of 3)
    
    # STEP 3: Get which page user wants to see
    page_number = request.GET.get('page')
    
    # STEP 4: Get the races for this specific page
    page_obj = paginator.get_page(page_number)
    
    # STEP 5: Prepare data for template
    context = {
        'races': page_obj,  # User's races for this page
        'is_paginated': page_obj.has_other_pages(),  # Multiple pages?
        'page_obj': page_obj,  # Pagination controls
    }
    
    # STEP 6: Show the "My Races" template with user's races
    return render(request, 'races/my_races.html', context)


@login_required
def delete_comment(request, comment_id):
    """
    VIEW 5: Delete Comment - Allow users to delete their own comments
    
    Only the comment author can delete their own comment
    """
    
    # STEP 1: Get the comment or return 404 if not found
    comment = get_object_or_404(Comment, id=comment_id)
    
    # STEP 2: Check if current user is the comment author
    if comment.author != request.user:
        messages.error(request, "You can only delete your own comments!")
        return redirect('race-detail', pk=comment.race.pk)
    
    # STEP 3: Store race pk before deleting comment
    race_pk = comment.race.pk
    
    # STEP 4: Delete the comment
    comment.delete()
    
    # STEP 5: Show success message and redirect back to race
    messages.success(request, "Your comment has been deleted!")
    return redirect('race-detail', pk=race_pk)


@login_required  # Only logged-in users can access edit functionality
def edit_race(request, pk):
    """
    VIEW 6: Edit Race - Allow race creator and admin to edit existing races
    
    This view handles both displaying the edit form AND processing the updates.
    Only the race creator or admin/staff can edit a race.
    """
    
    # STEP 1: Get the race from database (published races only)
    race = get_object_or_404(Race, pk=pk, status=1)
    
    # STEP 2: Check permissions - only race creator or admin can edit
    user_is_creator = race.created_by == request.user
    user_is_admin = request.user.is_staff or request.user.is_superuser
    
    if not (user_is_creator or user_is_admin):
        # User doesn't have permission to edit this race
        messages.error(request, "You can only edit races that you created!")
        return redirect('race-detail', pk=race.pk)
    
    # STEP 3: Check if user is submitting updated data (POST) or viewing (GET)
    if request.method == 'POST':
        # USER SUBMITTED THE FORM - Process the updated data
        
        # STEP 4: Create form instance with submitted data and existing race
        # request.POST = new text data (name, description, etc.)
        # request.FILES = new uploaded files (race image)
        # instance=race = tells form to update existing race, not create new
        form = RaceForm(request.POST, request.FILES, instance=race)
        
        # STEP 5: Check if all updated form data is valid
        if form.is_valid():
            # STEP 6: Save the updated race to database
            # No need to set created_by again - it stays the same
            updated_race = form.save()
            
            # STEP 7: Show success message with race name
            success_msg = f'Race "{updated_race.name}" updated successfully! 🎉'
            messages.success(request, success_msg)
            
            # STEP 8: Redirect user to the updated race's detail page
            return redirect('race-detail', pk=updated_race.pk)
        else:
            # STEP 9: Form has errors - show error message
            messages.error(request, "Please correct the errors below.")
    
    else:
        # USER IS JUST VIEWING THE EDIT PAGE - Show form with current race data
        # instance=race = pre-populate form fields with existing race data
        form = RaceForm(instance=race)
        
        # Ensure date field is properly formatted for HTML5 date input
        if race.race_date:
            date_str = race.race_date.strftime('%Y-%m-%d')
            form.fields['race_date'].widget.attrs['value'] = date_str
    
    # STEP 10: Prepare data for template
    context = {
        'form': form,           # Form with race data (for editing)
        'race': race,           # Original race object (for page title, etc.)
        'is_editing': True,     # Flag to help template know this is edit mode
    }
    
    # STEP 11: Show the edit race template with pre-filled form
    return render(request, 'races/edit_race.html', context)


# ==============================================================================
# ACCOUNT DELETION VIEWS
# ==============================================================================

@login_required
def request_account_deletion(request):
    """
    VIEW 7: Request Account Deletion - Allow users to request account deletion
    
    This view allows authenticated users to request deletion of their account.
    The request must be approved by an admin before the account is deleted.
    """
    
    # STEP 1: Check if user already has a pending deletion request
    existing_request = AccountDeletionRequest.objects.filter(
        user=request.user,
        status__in=['PENDING', 'APPROVED']
    ).first()
    
    if existing_request:
        # User already has a pending or approved deletion request
        messages.info(
            request,
            f"You already have a {existing_request.get_status_display().lower()} "
            f"account deletion request."
        )
        return redirect('deletion-status')
    
    # STEP 2: Handle form submission
    if request.method == 'POST':
        reason = request.POST.get('reason', '').strip()
        
        # STEP 3: Create the deletion request
        AccountDeletionRequest.objects.create(
            user=request.user,
            reason=reason
        )
        
        # STEP 4: Show success message
        messages.success(
            request,
            "Your account deletion request has been submitted for admin review. "
            "You will be notified via email when a decision is made."
        )
        
        # STEP 5: Redirect to status page
        return redirect('deletion-status')
    
    # STEP 6: Show the deletion request form
    return render(request, 'account/request_deletion.html')


@login_required
def deletion_status(request):
    """
    VIEW 8: Deletion Status - Show user their deletion request status
    
    This view shows the current status of the user's account deletion request.
    """
    
    # STEP 1: Get user's deletion request if it exists
    deletion_request = AccountDeletionRequest.objects.filter(
        user=request.user
    ).first()
    
    # STEP 2: Prepare context
    context = {
        'deletion_request': deletion_request,
    }
    
    # STEP 3: Show the status template
    return render(request, 'account/deletion_status.html', context)


@login_required
def cancel_deletion_request(request):
    """
    VIEW 9: Cancel Deletion Request - Allow users to cancel pending requests
    
    This view allows users to cancel their account deletion request
    if it's still pending admin review.
    """
    
    # STEP 1: Get user's pending deletion request
    deletion_request = AccountDeletionRequest.objects.filter(
        user=request.user,
        status='PENDING'
    ).first()
    
    if not deletion_request:
        messages.error(
            request,
            "You don't have a pending deletion request to cancel."
        )
        return redirect('race-list')
    
    # STEP 2: Handle cancellation
    if request.method == 'POST':
        # Delete the request
        deletion_request.delete()
        
        messages.success(
            request,
            "Your account deletion request has been cancelled."
        )
        
        return redirect('race-list')
    
    # STEP 3: Show confirmation page
    context = {
        'deletion_request': deletion_request,
    }
    return render(request, 'account/cancel_deletion.html', context)
