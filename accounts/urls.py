from django.conf import settings
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView, name='login'),
    path('logout/', auth_views.LogoutView, name='logout'),
    path('profile/', views.profile, name='profile'),
]