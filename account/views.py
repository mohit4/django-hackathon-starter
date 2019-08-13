from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView
from django.views.generic import DetailView

from .forms import UserRegisterForm
from .models import Profile
from app.models import Entity

# Creating a new user
class UserRegisterView(CreateView):
    '''
    New user register view
    '''
    form_class = UserRegisterForm
    success_message = 'User registered successfully! Please proceed to login.'
    success_url = reverse_lazy('account:login')
    template_name = 'account/register.html'

class UserLoginView(LoginView):
    '''
    User login view
    '''
    template_name = 'account/login.html'
    redirect_authenticated_user = True

class UserProfileView(DetailView):
    '''
    View details of user profile
    '''
    model = Profile
    template_name = 'account/user_profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        curr_user = self.object.user
        context["entity_count"] = len(Entity.objects.filter(user=curr_user))
        return context
    