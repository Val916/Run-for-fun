"""
ease add cCustom middleware for improving Best Practices Score and Cache Performance
"""
import re


class SecurityHeadersMiddleware:
    """
    Middleware to add security headers that improve Lighthouse
    Best Practices score and address cookie issues with third-party resources
    """
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        # Add security headers
        response['Referrer-Policy'] = 'strict-origin-when-cross-origin'
        response['Permissions-Policy'] = (
            'geolocation=(), microphone=(), camera=()'
        )
        
        # Cross-Origin Resource Policy for better cookie control
        response['Cross-Origin-Resource-Policy'] = 'cross-origin'
        
        # Additional security headers
        response['Cross-Origin-Embedder-Policy'] = 'unsafe-none'
        response['Cross-Origin-Opener-Policy'] = 'same-origin-allow-popups'
        
        return response


class MediaCacheMiddleware:
    """
    Middleware to add proper cache headers for media files (user uploads)
    This significantly improves repeat visit performance
    """
    
    def __init__(self, get_response):
        self.get_response = get_response
        # Pattern to match media files
        self.media_pattern = re.compile(
            r'^/media/.*\.(jpg|jpeg|png|gif|webp|svg|ico|css|js|woff|woff2|'
            r'ttf|eot|pdf|zip)$',
            re.IGNORECASE
        )

    def __call__(self, request):
        response = self.get_response(request)
        
        # Check if this is a media file request
        if self.media_pattern.match(request.path_info):
            # Add cache headers for media files
            # Cache for 30 days (2592000 seconds) - shorter than static files
            # since these might be updated by users
            response['Cache-Control'] = 'public, max-age=2592000, immutable'
            # 30 days from now
            response['Expires'] = 'Thu, 06 Nov 2025 00:00:00 GMT'
            
            # Add ETag for better cache validation
            if hasattr(response, 'content') and response.content:
                import hashlib
                etag = hashlib.md5(response.content).hexdigest()
                response['ETag'] = f'"{etag}"'
        
        return response