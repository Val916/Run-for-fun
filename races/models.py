from django.db import models         
from django.contrib.auth.models import User  
from cloudinary.models import CloudinaryField 
from django.urls import reverse      # Utility for generating URLs by name
from django.utils import timezone    # Utilities for time zone-aware datetimes


class Race(models.Model):
    """
    Race model represents a running event that users can create and view
    """
    
    # CHOICE FIELDS: Define dropdown options FIRST, before using them
    # Format: (database_value, display_value)
    
    DISTANCE_CHOICES = [
        ('5K', '5K (3.1 miles)'),
        ('HALF', 'Half Marathon (13.1 miles)'),
        ('FULL', 'Full Marathon (26.2 miles)'),
        ('ULTRA', 'Ultra Marathon (50K+)'),
        ('OTHER', 'Other Distance'),]

    DIFFICULTY_CHOICES = [
        ('EASY_PEASY', 'Easy-peasy'),
        ('ADULTS_ONLY', 'Adults Only'),
        ('CRAZY_TOUGH', 'Crazy Tough'),
        ('EXTREME_LAUGH', 'Extreme Laugh'),]
    
    STATUS_CHOICES = [
        (0, "Draft"),
        (1, "Published"),]

    # MODEL FIELDS start here
    name = models.CharField(
        max_length=200,
        help_text="Enter the race name")

    description = models.TextField(
        help_text="Describe the race, course, and any special details")
    distance = models.CharField(
        max_length=10,                     
        choices=DISTANCE_CHOICES,          
        default='OTHER',                      
        help_text="Select the race distance")
    
    custom_distance = models.CharField(
        max_length=50,                    
        blank=True,                        
        help_text="If 'Other Distance' selected, specify the exact distance")

    difficulty = models.CharField(
        max_length=20,                   
        choices=DIFFICULTY_CHOICES,        
        default='EASY_PEASY',                    
        help_text="Select the difficulty level of your crazy run")
    
    race_date = models.DateField(
        help_text="Set the race date")
    
    registration_link = models.URLField(
        blank=True,                       
        help_text="URL to external registration page")
    
    image = CloudinaryField(
        'image',                          
        blank=True,                      
        null=True,                        
        default='placeholder',            
        help_text="Upload a photo for this race (optional)")

    city = models.CharField(
        max_length=100,
        help_text="City name")

    latitude = models.DecimalField(            # for future map integration
        max_digits=9,
        decimal_places=6,
        blank=True,
        null=True,
        help_text="Latitude of race location (for map display)")
    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        blank=True,
        null=True,
        help_text="Longitude of race location (for map display)")
    
    country = models.CharField(                     
        max_length=50,
        default='UK',
        help_text="Country where race takes place")

    status = models.IntegerField(                  
        choices=STATUS_CHOICES,
        default=0,                        
        help_text="Current race status")
    
    approved = models.BooleanField(                  
        default=False,                     
        help_text="Whether this race has been approved by admin")

    approved_at = models.DateTimeField(              
        blank=True,
        null=True,
        help_text="When this race was approved by admin")
    
    approved_by = models.ForeignKey(User,              
        on_delete=models.SET_NULL,                     # Keep approval record even if admin user deleted
        related_name='approved_races',                 # Allows: admin.approved_races.all()
        blank=True,                                    
        null=True,
        help_text="Admin user who approved this race")
    
    created_by = models.ForeignKey(User,   
        on_delete=models.CASCADE,          
        related_name='created_races',      
        help_text="User who created this race")

    created_at = models.DateTimeField(auto_now_add=True, help_text="When this race was first created")
  #__________________________________________________________________________________________________________
    class Meta:
        """
        Meta class defines model-level options and behaviors
        These settings affect how Django handles the model
        """
        ordering = ['race_date']   #  (earliest date first)
        indexes = [
            models.Index(fields=['race_date']),  # Database indexes for better query performance
            models.Index(fields=['city']),         
            models.Index(fields=['status']),]
    
    # STRING REPRESENTATION - How races appear in lists and dropdowns
    def __str__(self):
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
        """
        return self.status == 1
    
    @property
    def is_visible_to_public(self):
        """
        Check if race is visible to all users (published AND approved)
        Returns True only if both published and approved by admin
        """
        return self.is_published and self.approved
    
    def is_visible_to_user(self, user):
        """
        Check if race is visible to a specific user
        - Public races: visible to everyone
        - Unapproved races: visible only to creator and admin
        """
        if self.is_visible_to_public:
            return True
        # Anonymous users can only see public races
        if not user.is_authenticated:
            return False
        # Admins can see all races
        if user.is_staff or user.is_superuser:
            return True
        # Race creators can see their own races
        if self.created_by == user:
            return True
        return False
    
    @property  
    def has_coordinates(self):
        """
        Check if race has latitude/longitude for map display
        Returns True if both lat and lng are set, False otherwise
        Use case: Only show map if coordinates exist
        """
        return self.latitude is not None and self.longitude is not None
    
    @property
    def days_until_race(self):
        """
        Calculate how many days until the race
        Returns number of days (can be negative if past)
        """
        time_diff = self.race_date - timezone.now().date()
        return time_diff.days
#__________________________________________________________________________________________________________

class Comment(models.Model):
    """
    COMMENT MODEL - User discussions on races
    
    This model allows users to leave comments on race pages.
    Comments create a community discussion around each race.
    
    RELATIONSHIPS:
    - Each comment belongs to ONE race (ForeignKey to Race)
    - Each comment has ONE author (ForeignKey to User)
    - Each race can have MANY comments (related_name='comments')
    """
    
    # RELATIONSHIP TO RACE - Which race this comment is about
    race = models.ForeignKey(
        Race,                           # Links to Race model
        on_delete=models.CASCADE,       # If race deleted, delete all its comments
        related_name='comments',        # Allows: race.comments.all()
        help_text="Which race this comment belongs to"
    )
    
    # RELATIONSHIP TO USER - Who wrote this comment
    author = models.ForeignKey(
        User,                           # Links to Django's User model
        on_delete=models.CASCADE,       # If user deleted, delete their comments
        help_text="User who wrote this comment"
    )

    
    # COMMENT CONTENT - The actual text of the comment
    body = models.TextField(
        max_length=1000,                # Limit to prevent spam/abuse
        help_text="Comment text (max 1000 characters)"
    )
    
    # TIMESTAMP - When comment was created
    created_on = models.DateTimeField(
        auto_now_add=True,              # Automatically set when comment created
        help_text="When comment was posted"
    )
    
    # MODERATION SYSTEM - Allow admin to hide inappropriate comments
    approved = models.BooleanField(
        default=True,                   # Auto-approve (change to False for moderation)
        help_text="Whether comment is approved for display"
    )
    
    class Meta:
        """
        META OPTIONS for Comment model
        """
        # ORDERING: Show newest comments first
        ordering = ['-created_on']     # Minus sign = descending order
        
        # DATABASE INDEXES: Speed up common queries
        indexes = [
            # Index for "get all comments for a race, newest first"
            models.Index(fields=['race', '-created_on']),
        ]
    
    # STRING REPRESENTATION - How comments appear in admin/lists
    def __str__(self):
        """
        Display format: "Comment by username on Race Name"
        Truncate long race names to keep it readable
        """
        race_name = self.race.name[:30] + "..." if len(self.race.name) > 30 else self.race.name
        return f"Comment by {self.author.username} on {race_name}"
    
    # CUSTOM METHODS for Comment model
    
    @property
    def is_recent(self):
        """
        Check if comment was posted in the last 24 hours
        Useful for highlighting new comments
        """
        from datetime import timedelta
        return timezone.now() - self.created_on < timedelta(hours=24)
    
    @property
    def short_body(self):
        """
        Return first 100 characters of comment for previews
        Useful in admin lists or comment summaries
        """
        return self.body[:100] + "..." if len(self.body) > 100 else self.body


class AccountDeletionRequest(models.Model):
    """
    ACCOUNT DELETION REQUEST MODEL - User account deletion with admin approval
    
    This model handles the complete account deletion workflow:
    1. User submits deletion request with optional reason
    2. Admin reviews and approves/rejects the request
    3. If approved, account is marked for deletion
    4. Final deletion is completed by admin action
    
    RELATIONSHIPS:
    - Each request belongs to ONE user (OneToOneField to User)
    - Each request can be reviewed by ONE admin (ForeignKey to User)
    - Users can only have ONE active deletion request at a time
    
    WORKFLOW STATES:
    PENDING → APPROVED/REJECTED → COMPLETED (if approved)
    """
    
    # STATUS CHOICES - Defines the deletion request workflow states
    # Format: (database_value, human_readable_display)
    STATUS_CHOICES = [
        ('PENDING', 'Pending Admin Review'),        # Initial state when user submits request
        ('APPROVED', 'Approved - Account Will Be Deleted'),    # Admin approved deletion
        ('REJECTED', 'Rejected - Account Will Not Be Deleted'), # Admin rejected deletion
        ('COMPLETED', 'Completed - Account Has Been Deleted'),  # Deletion process finished
    ]
    
    # USER RELATIONSHIP - Which user wants their account deleted
    user = models.OneToOneField(
        User,                                       # Links to Django's User model
        on_delete=models.CASCADE,                   # Delete request if user somehow deleted first
        related_name='deletion_request',            # Allows: user.deletion_request
        help_text="User requesting account deletion"
    )
    
    # REQUEST DETAILS - User's explanation for wanting deletion
    reason = models.TextField(
        max_length=500,                             # Reasonable limit for feedback
        help_text="User's reason for requesting account deletion",
        blank=True                                  # Optional field - user can skip this
    )
    
    # TIMESTAMP FIELDS - Track the deletion request timeline
    
    # When user first submitted the deletion request
    requested_at = models.DateTimeField(
        auto_now_add=True,                          # Automatically set when request created
        help_text="When the deletion was requested"
    )
    
    # When admin reviewed the request (approved or rejected)
    reviewed_at = models.DateTimeField(
        null=True,                                  # Empty until admin reviews
        blank=True,                                 # Optional in forms
        help_text="When admin reviewed the request"
    )
    
    # When the actual account deletion was completed
    completed_at = models.DateTimeField(
        null=True,                                  # Empty until deletion finished
        blank=True,                                 # Optional in forms
        help_text="When account deletion was completed"
    )
    
    # STATUS AND ADMIN REVIEW FIELDS
    
    # Current state of the deletion request
    status = models.CharField(
        max_length=20,                              # Longest choice is 'COMPLETED' (9 chars)
        choices=STATUS_CHOICES,                     # Must be one of the defined choices
        default='PENDING',                          # New requests start as pending
        help_text="Current status of deletion request"
    )
    
    # Which admin user reviewed this request
    reviewed_by = models.ForeignKey(
        User,                                       # Links to Django's User model
        on_delete=models.SET_NULL,                  # Keep record even if admin deleted
        null=True,                                  # Empty until reviewed
        blank=True,                                 # Optional in forms
        related_name='deletion_reviews',            # Allows: admin.deletion_reviews.all()
        help_text="Admin who reviewed this request"
    )
    
    # Internal admin notes about the deletion decision
    admin_notes = models.TextField(
        max_length=500,                             # Space for detailed admin feedback
        blank=True,                                 # Optional - admin can leave empty
        help_text="Internal admin notes about the deletion request"
    )

    class Meta:
        """
        META OPTIONS for AccountDeletionRequest model
        """
        # DISPLAY NAMES in Django admin
        verbose_name = "Account Deletion Request"
        verbose_name_plural = "Account Deletion Requests"
        
        # DEFAULT ORDERING: Show newest requests first
        ordering = ['-requested_at']               # Minus sign = descending order

    def __str__(self):
        """
        STRING REPRESENTATION - How deletion requests appear in admin lists
        Format: "Deletion request by username (Current Status)"
        """
        return f"Deletion request by {self.user.username} ({self.get_status_display()})"
    
    # PROPERTY METHODS - Convenient status checking
    
    @property
    def is_pending(self):
        """
        Check if request is still waiting for admin review
        Returns True if status is 'PENDING', False otherwise
        Usage: if deletion_request.is_pending: show_cancel_button()
        """
        return self.status == 'PENDING'
    
    @property
    def is_approved(self):
        """
        Check if request has been approved for deletion
        Returns True if status is 'APPROVED', False otherwise
        Usage: if deletion_request.is_approved: prepare_for_deletion()
        """
        return self.status == 'APPROVED'
    
    # ACTION METHODS - Handle status transitions with proper timestamps
    
    def approve(self, admin_user, notes=""):
        """
        APPROVE the deletion request - admin accepts user's deletion request
        
        Args:
            admin_user: The admin User object who is approving
            notes: Optional admin notes about the approval decision
            
        Updates:
            - Sets status to 'APPROVED'
            - Records which admin approved it
            - Sets the review timestamp
            - Saves admin notes
        """
        self.status = 'APPROVED'
        self.reviewed_by = admin_user
        self.reviewed_at = timezone.now()
        self.admin_notes = notes
        self.save()
    
    def reject(self, admin_user, notes=""):
        """
        REJECT the deletion request - admin denies user's deletion request
        
        Args:
            admin_user: The admin User object who is rejecting
            notes: Optional admin notes about the rejection reason
            
        Updates:
            - Sets status to 'REJECTED'
            - Records which admin rejected it
            - Sets the review timestamp
            - Saves admin notes (important for rejection reasons)
        """
        self.status = 'REJECTED'
        self.reviewed_by = admin_user
        self.reviewed_at = timezone.now()
        self.admin_notes = notes
        self.save()
    
    def complete(self):
        """
        COMPLETE the deletion process - mark that account has been deleted
        
        This method should be called AFTER the actual user account deletion
        to keep a record that the deletion was completed.
        
        Updates:
            - Sets status to 'COMPLETED'
            - Records completion timestamp
        """
        self.status = 'COMPLETED'
        self.completed_at = timezone.now()
        self.save()