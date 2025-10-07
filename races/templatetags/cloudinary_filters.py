"""
Custom template filters for handling Cloudinary images with better cookie control

These filters provide secure, privacy-focused image loading from Cloudinary
while maintaining compatibility with Django templates and reducing third-party
cookie issues that can affect Lighthouse scores and user privacy.
"""
from django import template

register = template.Library()


@register.filter
def cloudinary_secure(image_url):
    """
    Add security parameters to Cloudinary URLs to minimize cookie issues
    
    This filter takes a Cloudinary URL and adds optimization parameters
    that reduce tracking while improving performance:
    - dpr_auto: Automatically adjusts for device pixel ratio
    - f_auto: Automatically selects optimal image format (WebP, AVIF, etc.)
    - q_auto: Automatically optimizes image quality
    
    Args:
        image_url (str): The original Cloudinary image URL
        
    Returns:
        str: Enhanced URL with privacy and performance parameters
    """
    if not image_url or 'res.cloudinary.com' not in str(image_url):
        return image_url
    
    # Add parameters to reduce tracking and cookie issues
    if '?' in str(image_url):
        return f"{image_url}&dpr_auto=true&f_auto=true&q_auto=true"
    else:
        return f"{image_url}?dpr_auto=true&f_auto=true&q_auto=true"


@register.filter
def secure_cloudinary_url(cloudinary_field):
    """
    Generate a secure Cloudinary URL from a CloudinaryField
    
    This is the main filter used in templates to convert Cloudinary database
    fields into properly formatted URLs. It bypasses the standard .url property
    which was causing configuration errors after implementing privacy controls.
    
    The filter:
    1. Extracts the public_id from the CloudinaryField
    2. Uses cloudinary.utils to generate URLs with explicit configuration
    3. Adds security and optimization parameters
    4. Returns HTTPS URLs for enhanced security
    
    Usage in templates:
        {{ race.image|secure_cloudinary_url }}
    
    Args:
        cloudinary_field: A Django CloudinaryField instance from the database
        
    Returns:
        str: Complete HTTPS Cloudinary URL with optimization parameters,
             or empty string if field is invalid
    """
    if not cloudinary_field:
        return ""
    
    try:
        # Use cloudinary.utils to generate URL with explicit configuration
        # This bypasses the .url property that was causing "cloud_name" errors
        from cloudinary import utils
        
        # Get the public_id from the field - Cloudinary's internal identifier
        public_id = str(cloudinary_field)
        
        # Generate URL with security and performance parameters
        url, options = utils.cloudinary_url(
            public_id,
            secure=True,           # Force HTTPS for security
            dpr="auto",           # Auto device pixel ratio optimization
            f="auto",             # Auto format selection (WebP, AVIF, etc.)
            q="auto"              # Auto quality optimization
        )
        return url
    except Exception:
        # Fallback to empty string if there's any issue with URL generation
        # This prevents template crashes and allows fallback images to display
        return ""


@register.filter
def is_placeholder(cloudinary_field):
    """
    Check if a Cloudinary field contains a placeholder image
    
    This filter determines whether a CloudinaryField contains actual image
    content or just placeholder/default values. It's used in templates to
    decide whether to show the Cloudinary image or a local default image.
    
    The filter checks for:
    - Empty or None fields
    - Common placeholder strings like "placeholder", "sample", "default"
    - Empty string values
    
    Usage in templates:
        {% if race.image|is_placeholder %}
            <img src="{% static 'images/default.png' %}" alt="Default image">
        {% else %}
            <img src="{{ race.image|secure_cloudinary_url }}"
                 alt="{{ race.name }}">
        {% endif %}
    
    Args:
        cloudinary_field: A Django CloudinaryField instance from the database
        
    Returns:
        bool: True if the field contains placeholder content, False if it
              contains a real image that should be loaded from Cloudinary
    """
    if not cloudinary_field:
        return True
        
    # Convert to string to check the actual content
    field_str = str(cloudinary_field)
    
    # Check for common placeholder patterns and empty values
    return (
        not field_str or                              # Empty string
        field_str == "" or                            # Explicit empty string
        "placeholder" in field_str.lower() or        # Contains "placeholder"
        field_str in ["sample", "default", "placeholder"]  # Common defaults
    )