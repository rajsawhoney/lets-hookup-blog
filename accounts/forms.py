from django import forms

from django.contrib.auth.forms import UserCreationForm

from .models import UserModel

from django.contrib.auth.models import User



class UserForm(UserCreationForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Your Email Here...', }))
    username = forms.CharField(label='Username', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Your Username Here...'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your password here...'}))
    password2 = forms.CharField(label='Confirmed Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your confirmed password here...'}))

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ("email",)


class UserProfileForm(forms.ModelForm):
    about_me = forms.CharField(label='About Me', widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Something cool about you here...', 'rows': '4', 'cols': '60'}))

    qualifications = forms.CharField(label='Your Qualifications', widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Your Qualifications here...', 'rows': '2', 'cols': '60'}))

    profile_pic = forms.ImageField(
        label='Profile Pic', required=False,)

    class Meta:
        model = UserModel
        fields = ("about_me", "qualifications", "profile_pic",)
