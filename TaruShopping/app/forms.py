from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm,PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation
from app.models import Customer 

class CustomerRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta :
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {'email':'E-mail'}

        widgets = {'username': forms.TextInput(attrs={'class':"form-control"})}

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password = forms.CharField(label=_('password'), strip=False, 
    widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))

class MyPassChangeForm(PasswordChangeForm):
    Old_Password = forms.CharField(label=_('Old Password'),strip=False,
      widget=forms.PasswordInput(attrs=
      {'autocomplete':'current-pasword','autofocus':True,'class': 'form-control'}))
    New_Password1 = forms.CharField(label=_('New Password'),strip=False,
      widget=forms.PasswordInput(attrs=
      {'autocomplete':'new-pasword','autofocus':True,'class': 'form-control'}),
      help_text=password_validation.
      password_validators_help_text_html())
    New_Password2 = forms.CharField(label=_('Confirm Password'),strip=False,
      widget=forms.PasswordInput(attrs=
      {'autocomplete':'new-pasword','autofocus':True,'class': 'form-control'}))

class PassResetForm(PasswordResetForm):
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

class PassResetDone(SetPasswordForm):
        New_Password1 = forms.CharField(label=_('New Password'),
        widget=forms.PasswordInput(attrs=
        { 'class': 'form-control'}))
        New_Password2 = forms.CharField(label=_('Confirm Password'),
        widget=forms.PasswordInput(attrs=
        {'class': 'form-control'}))
    
class CustomerProfileForm(forms.ModelForm):
    class Meta :
        model = Customer
        fields = ['name', 'locality', 'city', 'zipcode','state']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'zipcode':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-control'}),
            
        }