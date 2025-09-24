from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Race
from .forms import RaceForm


def race_list(request):
    """Display list of all published races"""
    races = Race.objects.filter(status=1).order_by('race_date')
    
    # Pagination - show 9 races per page
    paginator = Paginator(races, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'races': page_obj,
        'is_paginated': page_obj.has_other_pages(),
        'page_obj': page_obj,
    }
    return render(request, 'races/race_list.html', context)


def race_detail(request, pk):
    """Display detailed view of a single race"""
    race = get_object_or_404(Race, pk=pk, status=1)
    return render(request, 'races/race_detail.html', {'race': race})


@login_required
def create_race(request):
    """Create a new race (login required)"""
    if request.method == 'POST':
        form = RaceForm(request.POST, request.FILES)
        if form.is_valid():
            race = form.save(commit=False)
            race.created_by = request.user
            race.status = 1  # Published
            race.save()
            messages.success(request, f'Race "{race.name}" created successfully!')
            return redirect('race-detail', pk=race.pk)
    else:
        form = RaceForm()
    
    return render(request, 'races/create_race.html', {'form': form})


@login_required
def my_races(request):
    """Display races created by the current user"""
    races = Race.objects.filter(created_by=request.user).order_by('-created_at')
    
    # Pagination for user's races
    paginator = Paginator(races, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'races': page_obj,
        'is_paginated': page_obj.has_other_pages(),
        'page_obj': page_obj,
    }
    return render(request, 'races/my_races.html', context)
