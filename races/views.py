# Import Django's built-in functions for web views
from django.shortcuts import render, get_object_or_404, redirect
# Import decorator that requires user to be logged in
from django.contrib.auth.decorators import login_required
# Import Django's message system for success/error notifications
from django.contrib import messages
# Import Django's pagination system to split long lists into pages
from django.core.paginator import Paginator
# Import our Race model from the current app
from .models import Race
# Import our custom form for creating/editing races
from .forms import RaceForm


def race_list(request):
    """
    VIEW 1: Homepage - Display list of all published races
    
    This view handles the main page where everyone can see all races.
    It shows only published races (status=1), not drafts (status=0).
    """
    
    # STEP 1: Get all published races from database
    # filter(status=1) = only get races with status "Published" 
    # order_by('race_date') = sort by race date (earliest first)
    races = Race.objects.filter(status=1).order_by('race_date')
    
    # STEP 2: Split races into pages (pagination)
    # This prevents showing 100+ races on one page
    paginator = Paginator(races, 5)  # Show 5 races per page
    
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
    }
    
    # STEP 6: Render the HTML template with our data
    # Django finds 'races/race_list.html' template and fills it with context data
    return render(request, 'races/race_list.html', context)


def race_detail(request, pk):
    """
    VIEW 2: Race Detail Page - Show full information about one race
    
    This view shows all details of a specific race when user clicks "View Details".
    The 'pk' parameter comes from the URL (e.g., /race/5/ means pk=5).
    """
    
    # STEP 1: Get the specific race from database
    # pk = primary key (unique ID number for each race)
    # get_object_or_404 means: find this race OR show 404 error page
    # status=1 ensures we only show published races, not drafts
    race = get_object_or_404(Race, pk=pk, status=1)
    
    # STEP 2: Send race data to the detail template
    # Template will display all race information (name, date, description, etc.)
    return render(request, 'races/race_detail.html', {'race': race})


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
            
            # STEP 6: Set race status to "Published" (1)
            race.status = 1  # Published (not draft)
            
            # STEP 7: Now save the complete race to database
            race.save()
            
            # STEP 8: Show success message to user
            messages.success(request, f'Race "{race.name}" created!')
            
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
    paginator = Paginator(races, 6)
    
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
