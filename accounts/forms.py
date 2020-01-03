from django import forms
from django.forms import ValidationError
from django.contrib.auth.models import User

class SignInForm(forms.Form):
    username = forms.CharField(label='',widget = forms.TextInput(attrs={'class':'form-control','Placeholder':'User Name'}))
    pwd = forms.CharField(label='',widget = forms.PasswordInput(attrs={'class':'form-control','Placeholder':'Password'}))

class RegisterForm(forms.Form):
    firstname = forms.CharField(label='',widget = forms.TextInput(attrs={'class':'form-control','Placeholder':'First Name'}))
    lastname = forms.CharField(label='',widget = forms.TextInput(attrs={'class':'form-control','Placeholder':'Last Name'}))
    username = forms.CharField(label='',widget = forms.TextInput(attrs={'class':'form-control','Placeholder':'User Name'}))
    email = forms.EmailField(label='',widget = forms.EmailInput(attrs={'class':'form-control','Placeholder':'Email ID'}))
    pwd = forms.CharField(label='',widget = forms.PasswordInput(attrs={'class':'form-control','Placeholder':'Password'}))
    cpwd = forms.CharField(label='',widget = forms.PasswordInput(attrs={'class':'form-control','Placeholder':'Confirm Password'}))

    def clean(self):       #server side validation(clean)
      if self.cleaned_data.get('pwd') != self.cleaned_data.get('cpwd'):
        raise ValidationError('Confirm Password does not match!')
      return self.cleaned_data

    def clean_username(self):
      if User.objects.filter(username__exact = self.cleaned_data.get('username')).exists():
          raise ValidationError('Username already in Use.')
      return self.cleaned_data.get('username')
    