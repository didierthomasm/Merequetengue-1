from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterPegosteadorForm(UserCreationForm):
    """
    For our next trick, we'll use Django's standard user creation form, the one used by admin application
    to create a new user. With this 2 things are resolve:

    * Validation of uniqueness of the username.
    * Password creation, that includes confirmation of the password and if the password is safe.

    Also, extending standard form to request email, first and last name from the get-go, instead of re-creating Django's
    admin site's flow.
    """

    first_name = forms.CharField(max_length=100, help_text='First Name')
    last_name = forms.CharField(max_length=100, help_text='Last Name')
    email = forms.EmailField(max_length=150, help_text='Email', required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
