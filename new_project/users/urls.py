from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('create', views.create, name='create'),
    path('english', views.english, name='english'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('registration', views.registration, name='registration'),
    path('profile', views.profile, name='profile'),
    path('changeprofile', views.changeprofile, name='changeprofile'),
    path('add_word', views.add_word, name='add_word'),
    path('createdict', views.createdict, name='createdict'),
    path('dicts', views.dicts, name='dicts'),
    path('watch_word', views.watch_word, name='watch_word'),
    path('test', views.test, name='test'),
]

