from django.urls import path

from .views import (
    SignUpView,
    LoginFormView
)

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginFormView.as_view(), name='login'),
]