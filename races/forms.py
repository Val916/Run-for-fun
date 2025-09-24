# Import Django's forms system for creating HTML forms
from django import forms
# Import our Race model to base the form on
from .models import Race


class RaceForm(forms.ModelForm):
    """
    RACE CREATION FORM
    
    This form automatically creates HTML form fields based on our Race model.
    It handles user input for creating and editing races.
    ModelForm means Django creates form fields that match our model fields.
    """
    
    class Meta:
        """
        Meta class tells Django how to build this form
        """
        # STEP 1: Tell Django which model this form is for
        model = Race
        
        # STEP 2: List which model fields to include in the form
        # These become form fields (text boxes, dropdowns, etc.)
        fields = [
            'name',              # Text input for race name
            'description',       # Large text area for race description
            'distance',          # Dropdown menu with distance choices
            'custom_distance',   # Text input for custom distance
            'difficulty',        # Dropdown menu with difficulty choices
            'race_date',         # Date picker for race date
            'city',              # Text input for city name
            'country',           # Text input for country name
            'registration_link', # URL input for registration website
            'image',             # File upload for race photo
            'latitude',          # Number input for map coordinates
            'longitude'          # Number input for map coordinates
        ]
        
        # STEP 3: Customize how each form field looks and behaves
        # Widgets control the HTML input type and styling
        widgets = {
            # Race name - Simple text input box
            'name': forms.TextInput(attrs={
                'class': 'form-control',        # Bootstrap CSS class
                'placeholder': 'Enter race name'  # Hint text in field
            }),
            
            # Race description - Large text area (multiple lines)
            'description': forms.Textarea(attrs={
                'class': 'form-control',        # Bootstrap CSS class
                'rows': 4,                      # 4 lines tall
                'placeholder': 'Describe the race, course, details'
            }),
            
            # Distance - Dropdown menu with preset choices
            'distance': forms.Select(attrs={
                'class': 'form-select'          # Bootstrap dropdown styling
            }),
            
            # Custom distance - Text input (only used if "Other" selected)
            'custom_distance': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., "15K", "Obstacle Course"'
            }),
            
            # Difficulty - Dropdown menu with difficulty levels
            'difficulty': forms.Select(attrs={
                'class': 'form-select'          # Bootstrap dropdown styling
            }),
            
            # Race date - Special date picker input
            'race_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'                  # Shows calendar picker
            }),
            
            # City - Simple text input
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'City name'
            }),
            
            # Country - Simple text input
            'country': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Country'
            }),
            
            # Registration link - URL input (validates web addresses)
            'registration_link': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://example.com/register'
            }),
            
            # Race image - File upload input (accepts only images)
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'             # Only allow image files
            }),
            
            # Latitude - Number input for map coordinates
            'latitude': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': 'any',                  # Allow decimal numbers
                'placeholder': '51.5074'        # London latitude example
            }),
            
            # Longitude - Number input for map coordinates  
            'longitude': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': 'any',                  # Allow decimal numbers
                'placeholder': '-0.1278'        # London longitude example
            }),
        }
    
    def clean(self):
        """
        CUSTOM FORM VALIDATION
        
        This function runs when user submits the form.
        It checks if the form data makes sense and shows errors if not.
        Django calls this automatically during form.is_valid().
        """
        
        # STEP 1: Get the basic cleaned data from Django
        # This runs all the default validations first
        cleaned_data = super().clean()
        
        # STEP 2: Get the specific fields we want to validate
        distance = cleaned_data.get('distance')          # Selected distance
        custom_distance = cleaned_data.get('custom_distance')  # Custom text
        
        # STEP 3: Check our custom business rule
        # Rule: If user selects "Other Distance", they MUST fill custom field
        if distance == 'OTHER' and not custom_distance:
            # Raise error that will be shown to user
            raise forms.ValidationError(
                "Please specify custom distance when 'Other' is selected."
            )
        
        # STEP 4: Return the validated data
        # This data goes to the view if validation passes
        return cleaned_data