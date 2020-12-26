from django.contrib import admin
from django.urls import path, include

from vote import views
from vote import views as vote_views
from django.contrib.auth import views as auth_views

from main.views import get_menu_context


app_name = 'vote'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<str:room_name>/', views.room, name='room'),
]
