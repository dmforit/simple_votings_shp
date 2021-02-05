import sys

from django.contrib.auth import authenticate, login
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserChangeForm, CustomUserCreationForm
from simple_votings.settings import EMAIL_HOST_USER

sys.path.append('..')

# TODO store email data securely


class UserCreationView(generic.CreateView):
    form_class = CustomUserCreationForm

    def form_valid(self, form):
        super().form_valid(form)
        form.save()
        email = self.request.POST['email']
        username = self.request.POST['username']
        password = self.request.POST['password1']
        send_mail('Регистрация на Honest Polls',
                  'Благодарим Вас, ' + username + ', за регистрацию на нашем сайте.\n Да прибудет с Вами демократия! \n Команда Honest Polls',
                  EMAIL_HOST_USER,
                  [email],
                  fail_silently=True,
                  )

        user = authenticate(username=username, password=password)
        login(self.request, user)
        return HttpResponseRedirect(self.get_success_url())
    success_url = reverse_lazy('index')
    template_name = 'registration/signup.html'


class UserChangeView(generic.UpdateView):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/edit_profile.html'

    def get_object(self, **kwargs):
        return self.request.user


class UserProfileView(generic.TemplateView):
    form_class = CustomUserChangeForm
    template_name = 'registration/profile.html'


class UserLoginView(auth_views.LoginView):
    form_class = AuthenticationForm
    template_name = 'registration/login.html'

    def form_valid(self, form):
        login(self.request, form.get_user())
        return HttpResponseRedirect(self.get_success_url())
