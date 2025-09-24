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
