from django.contrib import admin
from django.utils import timezone
from .models import Race, Comment, AccountDeletionRequest


@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    """ admin interface for Race model with approval system"""
    
    # What columns to show in the race list
    list_display = [
        'name', 
        'distance', 
        'race_date', 
        'city', 
        'status',
        'approved',
        'created_by'
    ]
    
    # Add filters in the right sidebar
    list_filter = [
        'approved',
        'status', 
        'distance',
        'race_date',
        'created_at'
    ]
    
    # Add search functionality
    search_fields = [
        'name',
        'city',
        'country',
        'created_by__username'
    ]
    
    # Add bulk actions for approval
    actions = ['approve_races', 'unapprove_races']
    
    # Group form fields logically
    fieldsets = (
        ('Basic Race Info', {
            'fields': (
                'name', 'description', 'distance', 'custom_distance',
                'difficulty', 'image'
            )
        }),
        ('When & Where', {
            'fields': ('race_date', 'city', 'country', 'latitude', 'longitude')
        }),
        ('Publication & Approval', {
            'fields': ('status', 'registration_link', 'approved')
        }),
        ('Approval Info', {
            'fields': ('approved_by', 'approved_at'),
            'classes': ('collapse',)  # Starts collapsed
        }),
        ('Creator Info', {
            'fields': ('created_by',),
            'classes': ('collapse',)  # Starts collapsed
        })
    )
    
    # Custom display methods
    def approval_status_display(self, obj):
        """Show approval status with colored badges"""
        if obj.approved:
            return "✅ Approved"
        else:
            return "⏳ Pending"
    approval_status_display.short_description = 'Approval Status'
    
    # Custom admin actions
    def approve_races(self, request, queryset):
        """Bulk action to approve selected races"""
        from django.utils import timezone
        
        updated = 0
        for race in queryset:
            if not race.approved:
                race.approved = True
                race.approved_by = request.user
                race.approved_at = timezone.now()
                race.save()
                updated += 1
        
        self.message_user(
            request,
            f'{updated} race(s) have been approved.'
        )
    approve_races.short_description = "Approve selected races"
    
    def unapprove_races(self, request, queryset):
        """Bulk action to unapprove selected races"""
        updated = queryset.update(
            approved=False,
            approved_by=None,
            approved_at=None
        )
        self.message_user(
            request,
            f'{updated} race(s) have been unapproved.'
        )
    unapprove_races.short_description = "Unapprove selected races"
    
    # Automatically set the creator to current user
    def save_model(self, request, obj, form, change):
        if not change:  # Only when creating new race
            obj.created_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Admin interface for Comment model"""
    
    # What columns to show in the comments list
    list_display = [
        'short_body',
        'author',
        'race',
        'created_on',
        'approved'
    ]
    
    # Add filters in the right sidebar
    list_filter = [
        'approved',
        'created_on',
        'race'
    ]
    
    # Add search functionality
    search_fields = [
        'body',
        'author__username',
        'race__name'
    ]
    
    # Order by newest first
    ordering = ['-created_on']
    
    # Custom display methods
    def short_body(self, obj):
        """Show first 50 characters of comment"""
        return obj.body[:50] + "..." if len(obj.body) > 50 else obj.body
    short_body.short_description = 'Comment'


@admin.register(AccountDeletionRequest)
class AccountDeletionRequestAdmin(admin.ModelAdmin):
    """Admin interface for Account Deletion Requests"""
    
    # What columns to show in the deletion requests list
    list_display = [
        'user',
        'status',
        'requested_at',
        'reviewed_by',
        'reviewed_at'
    ]
    
    # Add filters in the right sidebar
    list_filter = [
        'status',
        'requested_at',
        'reviewed_at'
    ]
    
    # Add search functionality
    search_fields = [
        'user__username',
        'user__email',
        'reason',
        'admin_notes'
    ]
    
    # Order by newest first
    ordering = ['-requested_at']
    
    # Make some fields read-only
    readonly_fields = [
        'user',
        'reason',
        'requested_at',
        'reviewed_at',
        'completed_at'
    ]
    
    # Group form fields logically
    fieldsets = (
        ('Request Details', {
            'fields': (
                'user', 'reason', 'requested_at'
            )
        }),
        ('Admin Review', {
            'fields': ('status', 'admin_notes')
        }),
        ('Review Info', {
            'fields': ('reviewed_by', 'reviewed_at', 'completed_at'),
            'classes': ('collapse',)  # Starts collapsed
        })
    )
    
    # Custom admin actions
    def approve_deletion(self, request, queryset):
        """Bulk action to approve selected deletion requests"""
        updated = 0
        for deletion_request in queryset.filter(status='PENDING'):
            deletion_request.approve(request.user, 
                                   "Approved via admin bulk action")
            updated += 1
        
        self.message_user(
            request,
            f'{updated} deletion request(s) have been approved.'
        )
    approve_deletion.short_description = "Approve selected deletion requests"
    
    def reject_deletion(self, request, queryset):
        """Bulk action to reject selected deletion requests"""
        updated = 0
        for deletion_request in queryset.filter(status='PENDING'):
            deletion_request.reject(request.user, 
                                  "Rejected via admin bulk action")
            updated += 1
        
        self.message_user(
            request,
            f'{updated} deletion request(s) have been rejected.'
        )
    reject_deletion.short_description = "Reject selected deletion requests"
    
    actions = ['approve_deletion', 'reject_deletion']
    
    # Automatically set the reviewer to current user when saving
    def save_model(self, request, obj, form, change):
        if change and 'status' in form.changed_data:
            if obj.status in ['APPROVED', 'REJECTED'] and not obj.reviewed_by:
                obj.reviewed_by = request.user
                obj.reviewed_at = timezone.now()
        super().save_model(request, obj, form, change)
