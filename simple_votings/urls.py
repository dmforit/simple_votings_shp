"""simple_votings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

from accounts import views as accounts_views
from main import views
from vote import views as vote_views
from django.contrib.auth import views as auth_views

from main.views import get_menu_context

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_page, name='index'),
    path('time/', views.time_page, name='time'),

    path('signup/', accounts_views.UserCreationView.as_view(
        extra_context={
            'menu': get_menu_context(),
            'pagename': 'Регистрация'}
    ), name='signup'),

    path('edit_profile/', accounts_views.UserChangeView.as_view(
        extra_context={
            'menu': get_menu_context(),
            'pagename': 'Редактирование профиля'}
    ), name='edit_profile'),

    path('profile/', accounts_views.UserProfileView.as_view(
        extra_context={
            'menu': get_menu_context(),
            'pagename': 'Профиль пользователя'}
    ), name='profile'),

    path('login/', auth_views.LoginView.as_view(
        extra_context={
            'menu': get_menu_context(),
            'pagename': 'Авторизация'}
    ), name='login'),
    path('vote/', vote_views.new_vote, name='vote'),
    path('vote/rooms/', include('vote.urls', namespace='vote')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# TODO serve avatars securely
