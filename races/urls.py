# Import Django's URL routing system
from django.urls import path
# Import our views from the current app (races app)
from . import views

# 
# URL PATTERNS - Maps web addresses to view functions
# 
# When user visits a URL, Django finds the matching pattern 
# and calls the corresponding view function.
#
urlpatterns = [
    # HOMEPAGE: '/' shows all races
    # path('', ...) = empty string matches root URL
    # views.race_list = function to call
    # name='race-list' = internal name for generating URLs
    path('', views.race_list, name='race-list'),
    
    # RACE DETAIL: '/race/5/' shows race with ID 5
    # <int:pk> = capture integer from URL as 'pk' parameter
    # Django passes pk=5 to views.race_detail(request, pk=5)
    path('race/<int:pk>/', views.race_detail, name='race-detail'),
    
    # CREATE RACE: '/create-race/' shows race creation form
    # Fixed URL (no parameters)
    path('create-race/', views.create_race, name='create-race'),
    
    # MY RACES: '/my-races/' shows current user's races
    # Requires login (handled by @login_required in view)
    path('my-races/', views.my_races, name='my-races'),
]