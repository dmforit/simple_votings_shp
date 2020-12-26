from django.shortcuts import render

def new_vote(request):
    return render(request, 'vote/new_vote.html', {})

def room(request, room_name):
    return render(request, 'vote/room.html', {
        'room_name': room_name
    })
