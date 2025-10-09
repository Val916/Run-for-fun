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
    
    # EDIT RACE: '/race/5/edit/' shows edit form for race with ID 5
    # <int:pk> = capture race ID from URL as 'pk' parameter
    # Django passes pk=5 to views.edit_race(request, pk=5)
    # Requires login (handled by @login_required in view)
    path('race/<int:pk>/edit/', views.edit_race, name='edit-race'),
    
    # DELETE RACE: '/race/5/delete/' shows delete confirmation for race with ID 5
    # <int:pk> = capture race ID from URL as 'pk' parameter
    # Django passes pk=5 to views.delete_race(request, pk=5)
    # Requires login (handled by @login_required in view)
    path('race/<int:pk>/delete/', views.delete_race, name='delete-race'),
    
    # CREATE RACE: '/create-race/' shows race creation form
    # Fixed URL (no parameters)
    path('create-race/', views.create_race, name='create-race'),
    
    # MY RACES: '/my-races/' shows current user's races
    # Requires login (handled by @login_required in view)
    path('my-races/', views.my_races, name='my-races'),
    
    # DELETE COMMENT: '/delete-comment/5/' deletes comment with ID 5
    # <int:comment_id> = capture comment ID from URL
    path('delete-comment/<int:comment_id>/',
         views.delete_comment,
         name='delete-comment'),
    
    # ACCOUNT DELETION URLs
    # REQUEST DELETION: '/request-deletion/' allows user to request account deletion
    path('request-deletion/', views.request_account_deletion, name='request-deletion'),
    
    # DELETION STATUS: '/deletion-status/' shows status of deletion request
    path('deletion-status/', views.deletion_status, name='deletion-status'),
    
    # CANCEL DELETION: '/cancel-deletion/' allows user to cancel pending request
    path('cancel-deletion/', views.cancel_deletion_request, name='cancel-deletion'),
]