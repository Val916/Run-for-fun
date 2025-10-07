"""
Custom middleware for improving Best Practices Score
"""


class SecurityHeadersMiddleware:
    """
    Middleware to add security headers that improve Lighthouse Best Practices score
    and address cookie issues with third-party resources like Cloudinary
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