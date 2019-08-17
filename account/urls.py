from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import UserRegisterView
from .views import UserLoginView
from .views import UserProfileView
from .views import ProfileUpdateView

app_name = 'account'

urlpatterns = [
    path('', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('user/<int:pk>/profile/', UserProfileView.as_view(), name='user-profile'),
    path('user/<int:pk>/profile/edit/', ProfileUpdateView.as_view(), name='edit-profile'),
]