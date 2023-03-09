from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accounts.views import RegisterPegosteadorView

# Using defaults in django.settings.
# * When no redirect URL is provided, or settings.LOGIN_URL is not set, settings.LOGIN_URL defaults to '/accounts/login'
#   Reference: https://docs.djangoproject.com/en/4.1/ref/settings/#std-setting-LOGIN_URL

app_name = 'accounts'
urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register_pegosteador/', RegisterPegosteadorView.as_view(), name='register_pegosteador'),
]
