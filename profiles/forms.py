from django import forms
from django.contrib.auth.models import User

from .models import Profile


class UserLoginForm(forms.Form):
    username = forms.CharField(label="Enter your username or email", max_length=100)
    password = forms.CharField(label="Enter your password", widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        user = User.objects.filter(username=username)
        if user.exists():
            if user.first().check_password(password):
                return cleaned_data
            else :
                self.add_error('password', 'Password is wrong')
        else:
            self.add_error('username', 'Username is not valid')




class UserCreationForm(forms.Form):
    username = forms.CharField(label="Enter your username", max_length=100)
    email = forms.EmailField(label="Enter your email", max_length=100)
    password = forms.CharField(label="Enter your password", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Confirm your password", widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password1 != password2:
            self.add_error('password','Passwords do not match')

        username = cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            self.add_error('username','Username already taken')

        email = cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            self.add_error('email','Email already registered')

class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'bio', 'avatar')
