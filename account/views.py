from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

from .forms import UserRegisterForm

# Create your views here.
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