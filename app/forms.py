from django import forms
from django.contrib import auth
from django.contrib.auth import password_validation
from django.contrib.auth.forms import PasswordResetForm, UserCreationForm,AuthenticationForm, UsernameField,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import password_changed
from django.forms import fields
from django.forms.widgets import Widget 
from django.utils.translation import gettext, gettext_lazy as _
from .models import Customer

class CustomerRegistrationForm(UserCreationForm):
    username = forms.CharField(label='username',widget=forms.TextInput(attrs=({'class': 'form-control'})) )
    password1 = forms.CharField(label='Password', 
    widget=forms.PasswordInput(attrs=({'class':'form-control'})))

    password2 = forms.CharField(label=' Confirm password(again)',
    widget=forms.PasswordInput(attrs=({'class':'form-control'})))
    email = forms.CharField(label='Email',
    widget=forms.EmailInput(attrs=({'class':'form-control'})))



class Meta:
    model = User
    fields = ['username','email','password1', 'password2']
    #labels ={'email':'Email'}

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs=({'autofocus':True, 'class':'form-control'})))
    password = forms.CharField(label=_('password'),strip=False, widget=forms.PasswordInput(attrs=({'autocomplete':True, 'class':'form-control'})))

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_("Old password"), strip=False, 
    widget=forms.PasswordInput(attrs={'autocomplete':'current-password',
    'autofocus':True, 'class':'form-control'}))
    new_password1 = forms.CharField(label=_("New password"), strip=False,
      widget=forms.PasswordInput(attrs={'autocomplete':'new password','autofocus':True, 
      'class':'form-control'}), help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm New Password"), strip=False,
    widget=forms.PasswordInput(attrs={'autocomplete':'new password', 'class': 'form-control'}))

class MyPasswordResetForm(PasswordResetForm):
    email = forms.CharField(label=_('Email'),max_length=256,
    widget=forms.EmailInput(attrs=({'autocomplete':'email','class':'form-control'})))

class MySetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_("New password"), strip=False,
      widget=forms.PasswordInput(attrs={'autocomplete':'new password','autofocus':True, 
      'class':'form-control'}), help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm New Password"), strip=False,
    widget=forms.PasswordInput(attrs={'autocomplete':'new password', 'class': 'form-control'}))

class CustomerProfileForm(forms.ModelForm):
    
    class Meta:
        model = Customer
       # fields = '__all__'
       # exclude = ['user']
       


        fields = ['name','locality','Division_Choice','city','zipcode']
        Widget = {'name':forms.TextInput(attrs={'class':'form-control'}),
        'locality':forms.TextInput(attrs={'class':'form-control'}),
        'Division':forms.Select(attrs={'class':'form-control'}),
        'city':forms.TextInput(attrs={'class':'form-control'}),
        'zipcode':forms.NumberInput(attrs={'class':'form-control'})
        }
     
       