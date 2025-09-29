from django.contrib import admin
from .models import Race, Comment


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
