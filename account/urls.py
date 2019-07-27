from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'account'

urlpatterns = [
    path('', LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]