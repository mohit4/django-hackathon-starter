from django.contrib.auth.views import LogoutView
from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import UserRegisterView, UserLoginView, ProfileDetailView, ProfileUpdateView

app_name = 'account'

urlpatterns = [
    path('', UserLoginView.as_view(), name='login'),
    path('account/logout/', LogoutView.as_view(), name='logout'),
    path('account/register/', UserRegisterView.as_view(), name='register'),
    path('account/<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),
    path('account/<int:pk>/update/', ProfileUpdateView.as_view(), name='profile-update'),
]
