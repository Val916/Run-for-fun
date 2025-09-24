from django.contrib import admin
from .models import Race


@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    """ admin interface for Race model"""
    
    # What columns to show in the race list
    list_display = [
        'name', 
        'distance', 
        'race_date', 
        'city', 
        'status',
        'created_by'
    ]
    
    # Group form fields logically
    fieldsets = (
        ('Basic Race Info', {
            'fields': ('name', 'description', 'distance', 'difficulty')
        }),
        ('When & Where', {
            'fields': ('race_date', 'city', 'country', 'latitude', 'longitude')
        }),
        ('Registration', {
            'fields': ('registration_link', 'status')
        }),
        ('Creator Info', {
            'fields': ('created_by',),
            'classes': ('collapse',)  # Starts collapsed
        })
    )
    
    # Automatically set the creator to current user
    def save_model(self, request, obj, form, change):
        if not change:  # Only when creating new race
            obj.created_by = request.user
        super().save_model(request, obj, form, change)
