from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from vote.models import Vote


def new_vote(request):
    title = request.GET.get('title', None)
    options = request.GET.get('options', None)

    if title and options:
        list_options = list(map(str, options.split('\n')))
        for i in range(len(list_options) - 1):
            list_options[i] = list_options[i][:-1]

        list_voters = [[]] * len(list_options)

        v = Vote(title=title, options=str(list_options), voters=str(list_voters))
        v.save()

        return redirect('rooms/' + str(v.id))

    return render(request, 'vote/new_vote.html')


def room(request, room_name):
    selected = request.GET.get('option', None)
    data = Vote.objects.get(id=room_name)

    current_user_id = request.user.id

    if selected and current_user_id:
        selected = int(selected)
        selected -= 1
        voters = data.get_voters()
        for v in voters:
            for i in range(len(v)):
                if int(v[i]) == current_user_id:
                    v.pop(i)
                    break

        voters[selected].append(current_user_id)
        data.voters = str(voters)
        data.save()

    context = {'data': data}

    return render(request, 'vote/room.html', context)


def fav_view(request, pk):
    vote = get_object_or_404(Vote, id=request.POST.get('vote_id'))
    request.user.fav_votes.add(vote.id)
    return HttpResponseRedirect(reverse('vote:room', args=[str(pk)]))

# TODO voting pages as layout extension
# TODO vote can be created by unauthorised user
# TODO add design to votes
