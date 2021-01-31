from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from vote.models import Vote


# Create your views here.

def favorites(request):
    ctx = Vote.objects.all
    return render(request, "favorites/favorites.html", {"all": ctx})


def fav_view_remove(request):
    vote = get_object_or_404(Vote, id=request.POST.get('vote_id'))
    request.user.fav_votes.remove(vote.id)
    return HttpResponseRedirect(reverse('favorites'))
