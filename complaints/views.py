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
        context['has_data'] = True
        mail_admins(
            'Жалоба от пользователя',
            'Имя пользователя: {0}\nПочта пользователя: {1}\nЖалобы: {2}'.format(request.user.username, request.user.email, context['complaint_text']),
            fail_silently=True
        )
        return render(request, 'complaints/complaints.html', context)
    elif request.method == 'GET':
        context['form'] = form
        context['has_data'] = False

    return render(request, 'complaints/complaints.html', context)
