from django.shortcuts import render, redirect
from vote.models import Vote


def new_vote(request):
    title = request.GET.get('title', None)
    options = request.GET.get('options', None)

    if title and options:
        list_options = list(map(str, options.split('\n')))
        for i in range(len(list_options) - 1):
            list_options[i] = list_options[i][:-1]

        list_votes = [0] * len(list_options)

        v = Vote(title=title, options=str(list_options), votes=str(list_votes))
        v.save()
        print(v.id)

        return redirect('rooms/' + str(v.id))

    return render(request, 'vote/new_vote.html')


def room(request, room_name):
    data = Vote.objects.get(id=room_name)
    context = {'data': data}

    return render(request, 'vote/room.html', context)

# TODO voting pages as layout extension
# TODO add bootstrap to base.html
