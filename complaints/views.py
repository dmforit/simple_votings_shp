from django.shortcuts import render
from complaints.forms import ComplaintForm
from django.core.mail import send_mail, mail_admins
from simple_votings.settings import EMAIL_HOST_USER
from accounts.views import UserCreationView
from main.views import get_menu_context


def complaint_page(request):
    context = {
        'pagename': 'Жалобы',
        'menu': get_menu_context(),
    }

    form = ComplaintForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        context['complaint_text'] = form.cleaned_data.get('text')
        context['title'] = form.cleaned_data.get('title')
        context['has_data'] = True
        send_mail('Жалоба от пользователя',
                  'Имя пользователя: {0}\nПочта пользователя: {1}\nЗаголовок: {2}\nЖалобы: {3}'.format(request.user.username, request.user.email, context['title'], context['complaint_text']),
                  EMAIL_HOST_USER,
                  [request.user.email],
                  fail_silently=True,
        )
        send_mail('Жалоба от пользователя',
                  'Имя пользователя: {0}\nПочта пользователя: {1}\nЗаголовок: {2}\nЖалобы: {3}'.format(request.user.username, request.user.email, context['title'], context['complaint_text']),
                  EMAIL_HOST_USER,
                  [EMAIL_HOST_USER],
                  fail_silently=True,
        )
        return render(request, 'complaints/complaints.html', context)
    elif request.method == 'GET':
        context['form'] = form
        context['has_data'] = False

    return render(request, 'complaints/complaints.html', context)
