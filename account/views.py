from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.
class UserRegisterView(CreateView):
    '''
    New user register view
    '''
    form_class = UserCreationForm
    success_message = 'User registered successfully! Please proceed to login.'
    success_url = reverse_lazy('account:login')
    template_name = 'account/register.html'