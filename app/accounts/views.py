from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView

from .forms import RegistrationForm


class SignUpView(SuccessMessageMixin, CreateView):
    """
    Register view
    """
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    success_message = 'Registeration completed successfully! Please login to continue.'


class LoginFormView(SuccessMessageMixin, LoginView):
    """
    View for logging in to the system
    """
    template_name = 'registration/login.html'
    success_url = ''
    success_message = 'Logged in successfully!'