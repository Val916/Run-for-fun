"""
Custom template filters for handling Cloudinary images with better cookie control
"""
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def cloudinary_secure(image_url):
    """
    Add security parameters to Cloudinary URLs to minimize cookie issues
    """
    if not image_url or 'res.cloudinary.com' not in str(image_url):
        return image_url
    
    # Add parameters to reduce tracking and cookie issues
    if '?' in str(image_url):
        return f"{image_url}&dpr_auto=true&f_auto=true&q_auto=true"
    else:
        return f"{image_url}?dpr_auto=true&f_auto=true&q_auto=true"


@register.filter  
def img_with_security(image_url, alt_text=""):
    """
    Generate an img tag with security attributes for Cloudinary images
    """
    if not image_url:
        return ""
    
    secure_url = cloudinary_secure(image_url)
    
    img_tag = f'''<img src="{secure_url}" 
                       alt="{alt_text}"
                       crossorigin="anonymous" 
                       referrerpolicy="no-referrer-when-downgrade"
                       loading="lazy">'''
    
    return mark_safe(img_tag)