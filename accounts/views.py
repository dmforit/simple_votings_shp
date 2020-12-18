from django.contrib.auth.forms import UserCreationForm, UserChangeForm, User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic


class UserSignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('index')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return redirect('profile')


class UserEditProfileForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
        )


class UserEditProfileView(generic.UpdateView):
    form_class = UserEditProfileForm
    success_url = reverse_lazy('index')
    template_name = 'registration/edit_profile.html'

    def get_object(self, **kwargs):
        return self.request.user


class UserProfileView(generic.TemplateView):
    form_class = UserEditProfileForm
    template_name = 'registration/profile.html'

