from django.contrib import admin

from .models import Race, RaceRegistration


@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'distance', 'race_date', 'city', 'status',
        'max_participants', 'spots_remaining'
    ]
    list_filter = ['distance', 'difficulty', 'status', 'city', 'race_date']
    search_fields = ['name', 'city', 'location']
    date_hierarchy = 'race_date'
    readonly_fields = ['created_at', 'updated_at', 'spots_remaining']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'description', 'distance', 'difficulty')
        }),
        ('Schedule', {
            'fields': (
                'race_date', 'registration_open', 'registration_close'
            )
        }),
        ('Location', {
            'fields': ('location', 'city', 'state', 'country')
        }),
        ('Registration', {
            'fields': (
                'max_participants', 'registration_fee', 'status'
            )
        }),
        ('Metadata', {
            'fields': ('created_by', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        })
    )


@admin.register(RaceRegistration)
class RaceRegistrationAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'race', 'registered_at', 'tshirt_size',
        'finish_time', 'position'
    ]
    list_filter = ['race', 'registered_at', 'tshirt_size']
    search_fields = ['user__username', 'race__name']
    readonly_fields = ['registered_at']
    
    fieldsets = (
        ('Registration', {
            'fields': ('race', 'user', 'registered_at')
        }),
        ('Runner Details', {
            'fields': (
                'emergency_contact', 'emergency_phone', 'tshirt_size'
            )
        }),
        ('Race Results', {
            'fields': ('finish_time', 'position'),
            'description': 'Filled after race completion'
        })
    )
