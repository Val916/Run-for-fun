from django import forms
from .models import Race


class RaceForm(forms.ModelForm):
    """Form for creating and editing races"""
    
    class Meta:
        model = Race
        fields = [
            'name', 'description', 'distance', 'custom_distance', 
            'difficulty', 'race_date', 'city', 'country',
            'registration_link', 'image', 'latitude', 'longitude'
        ]
        
        # Custom widgets for better styling and user experience
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter race name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Describe the race, course, and any special details'
            }),
            'distance': forms.Select(attrs={
                'class': 'form-select'
            }),
            'custom_distance': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g., "15K", "Obstacle Course", "Trail Run"'
            }),
            'difficulty': forms.Select(attrs={
                'class': 'form-select'
            }),
            'race_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'City name'
            }),
            'country': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Country'
            }),
            'registration_link': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://example.com/register'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            }),
            'latitude': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': 'any',
                'placeholder': '51.5074'
            }),
            'longitude': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': 'any',
                'placeholder': '-0.1278'
            }),
        }
    
    def clean(self):
        """Custom validation for the form"""
        cleaned_data = super().clean()
        distance = cleaned_data.get('distance')
        custom_distance = cleaned_data.get('custom_distance')
        
        # If "Other" is selected, custom_distance must be provided
        if distance == 'OTHER' and not custom_distance:
            raise forms.ValidationError(
                "Please specify the custom distance when 'Other Distance' is selected."
            )
        
        return cleaned_data