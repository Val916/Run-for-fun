# Image Usage Guide

## Static Images (Design/Fixed Images)
Put images in: static/images/
- logos/ - for site logos
- backgrounds/ - for background images  
- icons/ - for icons and small graphics

Usage in templates:
{% load static %}
<img src="{% static 'images/logos/mylogo.png' %}" alt="Logo">

## Media Images (User Uploads)
Put images in: media/race_images/
These are uploaded by users when creating races.

Usage in templates:
<img src="{{ race.image.url }}" alt="{{ race.name }}">

## File Formats Supported:
- .jpg, .jpeg
- .png  
- .gif
- .webp