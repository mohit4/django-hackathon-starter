from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

from .forms import UserRegistrationForm
from .models import Profile


class UserRegisterView(CreateView):
    """
    View for registering a user
    """
    form_class = UserRegistrationForm
    success_url = reverse_lazy('account:login')
    template_name = 'account/register.html'


class UserLoginView(LoginView):
    """
    View for logging a user
    """
    template_name = 'account/login.html'
    redirect_authenticated_user = True


class ProfileDetailView(DetailView):
    """
    View for accessing a user profile details
    """
    template_name = 'account/profile_detail.html'
    model = Profile


class ProfileUpdateView(UpdateView):
    """
    View for updating a user profile details
    """
    template_name = 'account/profile_form.html'
    model = Profile
    fields = ('bio', 'website',)
