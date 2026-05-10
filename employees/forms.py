from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Employee


# User Registration Form
class UserForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# Employee Form
class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = [
            'phone',
            'address',
            'photo',
            'document'
        ]