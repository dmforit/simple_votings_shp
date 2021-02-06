from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from vote.models import Vote


def new_vote(request):
    title = request.GET.get('title', None)
    options = request.GET.get('options', None)
    vote_type = request.GET.get('type', None)

    if title and options:
        list_options = list(map(str, options.split('\n')))
        for i in range(len(list_options) - 1):
            list_options[i] = list_options[i][:-1]

        list_voters = [[]] * len(list_options)

        v = Vote(title=title, options=str(list_options), voters=str(list_voters),
                 vote_type=vote_type, author=request.user)
        v.save()
        request.user.own_votes.add(v.id)

        return redirect('rooms/' + str(v.id))
    return render(request, 'vote/new_vote.html')


def room(request, room_name):
    request_data = request.POST
    data = Vote.objects.get(id=room_name)
    current_user_id = request.user.id

    if 'option' in dict(request_data):
        selected = dict(request_data)['option']
    else:
        selected = None

    if selected and current_user_id:
        voters = data.get_voters()
        for v in voters:
            for i in range(len(v)):
                if int(v[i]) == current_user_id:
                    v.pop(i)
                    break

        for select in selected:
            select = int(select)
            select -= 1
            voters[select].append(current_user_id)

        data.voters = str(voters)
        data.save()

    context = {'data': data}
    return render(request, 'vote/room.html', context)


def fav_view(request, pk):
    vote = get_object_or_404(Vote, id=request.POST.get('vote_id'))
    request.user.fav_votes.add(vote.id)
    return HttpResponseRedirect(reverse('vote:room', args=[str(pk)]))


def own_votes_view(request):
    if request.method == "POST":
        vote = get_object_or_404(Vote, id=request.POST.get('vote_id'))
        request.user.own_votes.remove(vote.id)
        vote.delete()
        return HttpResponseRedirect(reverse('own_votes'))
    if request.method == "GET":
        ctx = request.user.own_votes.all
        return render(request, "vote/own_votes.html", {"all": ctx})
    return render(request, "vote/own_votes.html")


def all_votes_view(request):
    votes = Vote.objects.all()
    context = {'votes': votes}
    if request.method == "POST":
        vote = get_object_or_404(Vote, id=request.POST.get('vote_id'))
        request.user.fav_votes.add(vote.id)
    return render(request, 'vote/all_votes.html', context)
