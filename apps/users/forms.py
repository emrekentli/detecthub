from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from .models import CustomUser as User

GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female')
]

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    gender = forms.ChoiceField(choices=GENDER_CHOICES)

    class Meta:
        model = User
        fields = ['username', 'email', 'gender', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
