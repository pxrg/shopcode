from django import forms
from django.contrib.auth.models import User


class GenerateUsersForm(forms.Form):
    pass


class RegisterForm(forms.ModelForm):
    domain_url = forms.CharField(max_length=50)
    description = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ('first_name', 'username', 'email', 'password',
                  'domain_url', 'description')
