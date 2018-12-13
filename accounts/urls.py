from django.conf import settings
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(
        template_name='accounts/login_form.html',
        authentication_form=LoginForm,
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        next_page=settings.LOGIN_URL
    ), name='logout'),
    path('profile/', views.profile, name='profile'),
]