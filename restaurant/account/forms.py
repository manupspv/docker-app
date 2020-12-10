from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserSignUpForm(UserCreationForm):
    first_name = forms.CharField(label='firstname',widget=forms.TextInput(attrs={'placeholder':'First Name','class':'form-control'}))
    last_name = forms.CharField(label='lastname',widget=forms.TextInput(attrs={'placeholder':'Last Name','class':'form-control'}))
    username = forms.CharField(label='username',widget=forms.TextInput(attrs={'placeholder':'Username','class':'form-control'}))
    email = forms.EmailField(label='email',widget=forms.TextInput(attrs={'placeholder':'Email','class':'form-control'}))
    password1 = forms.CharField(label='password1',widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password','class':'form-control'}))
    password2 = forms.CharField(label='password2',widget=forms.PasswordInput(attrs={'placeholder': 'Repeat Password','class':'form-control'}))


    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='username',widget=forms.TextInput(attrs={'placeholder':'Username','class':'form-control'}))
    password = forms.CharField(label='password',widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password','class':'form-control'}))