from django.db import models         # Django ORM: model definitions
from django.contrib.auth.models import User  # Built-in user model for authentication
from django.urls import reverse      # Utility for generating URLs by name
from django.utils import timezone    # Utilities for time zone-aware datetimes


class Race(models.Model):
    """Model representing a running race"""
    
    # CHOICE FIELDS: Define dropdown options for consistency
    # Format: (database_value, display_value)
    
    # Race distances - covers most common running race distances
    DISTANCE_CHOICES = [
        ('5K', '5K (3.1 miles)'),      # Most popular beginner distance
        ('HALF', 'Half Marathon (13.1 miles)'),  # Very popular distance
        ('FULL', 'Full Marathon (26.2 miles)'),  # Classic marathon
        ('ULTRA', 'Ultra Marathon (50K+)'),      # Extreme distances
        ('OTHER', 'Other Distance'),             # Custom distances
    ]
    
    # Difficulty levels help runners choose appropriate races

    DIFFICULTY_CHOICES = [
        ('EASY', 'Easy'),                   # Flat, beginner-friendly
        ('ADULT_ONLY', 'Adult Only'),       # Some alcohol involved
        ('CRAZY_TOUGH', 'Crazy Tough'),     # Challenging even for pros
        ('EXTREMELY_FUNNY', 'Extremely Funny'),  # Very interesting conditions
    ]
    

    # Status tracks the race lifecycle
    STATUS_CHOICES = [
        (0, "Draft"),
        (1, "Published"),
    ]
    
    # BASIC RACE INFORMATION FIELDS
    
    # Race name - CharField for short text, required field
    name = models.CharField(
        max_length=200,                   
        help_text="Enter the race name"    # Shows in admin forms
    )
    
    # Detailed description - TextField for longer text, no length limit
    description = models.TextField(
        help_text="Describe the race, course, and any special details"
    )
    
    # Race distance - uses our DISTANCE_CHOICES from above
    distance = models.CharField(
        max_length=10,                     # Enough for our choice codes
        choices=DISTANCE_CHOICES,          
        default='OTHER',                      
        help_text="Select the race distance"
    )
    
    # Race difficulty - uses our DIFFICULTY_CHOICES from above  
    difficulty = models.CharField(
        max_length=20,                     # Increased for your longer choice names
        choices=DIFFICULTY_CHOICES,        
        default='EASY',                    
        help_text="Select the difficulty level"
    )
    
    # DATE AND TIME FIELDS
    
    race_date = models.DateField(
        help_text="Set the race date"
    )
    
    # Link to external registration page
    registration_link = models.URLField(
        blank=True,                       
        help_text="URL to external registration page"
    )

    
    # LOCATION FIELDS
    city = models.CharField(
        max_length=100,
        help_text="City name"
    )

    # Latitude and Longitude for map integration (optional, but recommended)
    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        blank=True,
        null=True,
        help_text="Latitude of race location (for map display)"
    )
    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        blank=True,
        null=True,
        help_text="Longitude of race location (for map display)"
    )
    
    # Country (defaults to UK but can be changed)
    country = models.CharField(
        max_length=50,
        default='UK',
        help_text="Country where race takes place"
    )
    
    # Race status
    status = models.IntegerField(
        choices=STATUS_CHOICES,
        default=0,                         # Default to Draft
        help_text="Current race status"
    )
    
    # METADATA FIELDS
    # Who created this race (ForeignKey creates relationship to User model)
    created_by = models.ForeignKey(
        User,                              # Links to Django's built-in User model
        on_delete=models.CASCADE,          # If user deleted, delete their races
        related_name='created_races',      # Allows: user.created_races.all()
        help_text="User who created this race"
    )
    
    # When this race record was first created
    created_at = models.DateTimeField(
        auto_now_add=True,                 
        help_text="When this race was first created"
    )
    
    class Meta:
        """
        Meta class defines model-level options and behaviors
        These settings affect how Django handles the model
        """
        # Default ordering when querying races (earliest date first)
        ordering = ['race_date']   
        
        # Database indexes for better query performance
        indexes = [
            models.Index(fields=['race_date']),    
            models.Index(fields=['city']),         
            models.Index(fields=['status']),       
        ]
    
    # STRING REPRESENTATION - How races appear in lists and dropdowns
    def __str__(self):
        """
        Returns human-readable string representation of the race
        This appears in admin lists, dropdowns, and when printing race objects
        Format: "Race Name - DD/MM/YYYY" (European format)
        """
        return f"{self.name} - {self.race_date.strftime('%d/%m/%Y')}"
    

    # MODEL METHODS AND PROPERTIES
    
    def get_absolute_url(self):
        """
        Generate URL for this race's detail page
        Used by Django to create links to individual race pages
        Requires 'race-detail' URL pattern in urls.py
        """
        return reverse('race-detail', kwargs={'pk': self.pk})
    
    @property
    def is_published(self):
        """
        Check if race is published and visible to public
        Returns True if status is 1 (Published), False if 0 (Draft)
        
        Usage: race.is_published (no parentheses needed)
        """
        return self.status == 1
    
    
    @property  
    def has_coordinates(self):
        """
        Check if race has latitude/longitude for map display
        Returns True if both lat and lng are set, False otherwise
        
        Usage: race.has_coordinates
        Use case: Only show map if coordinates exist
        """
        return self.latitude is not None and self.longitude is not None
    
    
    @property
    def days_until_race(self):
        """
        Calculate how many days until the race
        Returns number of days (can be negative if past)
        
        Usage: race.days_until_race
        Template: "Race in {{ race.days_until_race }} days"
        """
        time_diff = self.race_date - timezone.now().date()
        return time_diff.days