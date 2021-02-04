from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from vote.models import Vote
from accounts.models import CustomUser


# Create your views here.


def favorites(request):
    if request.method == "POST":
        vote = get_object_or_404(Vote, id=request.POST.get('vote_id'))
        request.user.fav_votes.remove(vote.id)
        return HttpResponseRedirect(reverse('favorites'))
    if request.method == "GET":
        ctx = request.user.fav_votes.all
        return render(request, "favorites/favorites.html", {"all": ctx})
    return render(request, "favorites/favorites.html")
