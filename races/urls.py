from django.urls import path
from . import views

urlpatterns = [
    path('', views.race_list, name='race-list'),
    path('race/<int:pk>/', views.race_detail, name='race-detail'),
    path('create-race/', views.create_race, name='create-race'),
    path('my-races/', views.my_races, name='my-races'),
]