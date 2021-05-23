from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin

from .forms import UserRegistrationForm
from .models import Profile


class UserRegisterView(SuccessMessageMixin, CreateView):
    """
    View for registering a user
    """
    form_class = UserRegistrationForm
    success_url = reverse_lazy('account:login')
    template_name = 'account/register.html'
    success_message = 'Registered user successfully! Login to continue...'


class UserLoginView(SuccessMessageMixin, LoginView):
    """
    View for logging a user
    """
    template_name = 'account/login.html'
    redirect_authenticated_user = True
    success_message = 'Logged in successfully!'


class ProfileDetailView(DetailView):
    """
    View for accessing a user profile details
    """
    template_name = 'account/profile_detail.html'
    model = Profile


class ProfileUpdateView(SuccessMessageMixin, UpdateView):
    """
    View for updating a user profile details
    """
    template_name = 'account/profile_form.html'
    model = Profile
    fields = ('bio', 'website',)
    success_message = 'Profile updated successfully!'


class ProfileListView(ListView):
    """
    Listing all the users
    """
    template_name = 'account/profile_list.html'
    model = Profile
    context_object_name = 'profiles'
