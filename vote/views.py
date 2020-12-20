from django.shortcuts import render

def new_vote(request):
    return render(request, 'vote/new_vote.html', {})
