from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import UserRegisterView
from .views import UserLoginView
from .views import UserProfileView

app_name = 'account'

urlpatterns = [
    path('', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('user/<int:pk>/profile/', UserProfileView.as_view(), name='user-profile'),
]