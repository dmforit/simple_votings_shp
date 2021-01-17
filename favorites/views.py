from django.shortcuts import render
from vote.models import Vote

# Create your views here.

def favorites(request):
    ctx = Vote.objects.all

    return render(request, "favorites/favorites.html", {"all": ctx})
