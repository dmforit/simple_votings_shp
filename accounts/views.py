from django.contrib.auth.forms import UserCreationForm, UserChangeForm, User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserChangeForm, CustomUserCreationForm


class UserCreationView(generic.CreateView):
    form_class = CustomUserCreationForm

    def form_valid(self, form):
        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return redirect('profile')

    success_url = reverse_lazy('index')
    template_name = 'registration/signup.html'


class UserChangeView(generic.UpdateView):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('index')
    template_name = 'registration/edit_profile.html'

    def get_object(self, **kwargs):
        return self.request.user


class UserProfileView(generic.TemplateView):
    form_class = CustomUserChangeForm
    template_name = 'registration/profile.html'

