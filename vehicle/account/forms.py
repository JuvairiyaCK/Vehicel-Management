from django import forms
from django.contrib.auth.models import User
# from django.core.exceptions import ValidationError
from .models import Vehicle
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import password_validation




class RegisterForm(UserCreationForm):
    password1 = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password","class":"form-control"}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=("Password confirmation"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password","class":"form-control"}),
        strip=False,
        help_text=("Enter the same password as before, for verification."),
    )
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password1","password2"]
        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "password1":forms.TextInput(attrs={"class":"form-control"}),
            "password2":forms.TextInput(attrs={"class":"form-control"})
        }


class LogForm(forms.Form):
    username=forms.CharField(max_length=100,widget=forms.TextInput(attrs={"class":"form-control"}),)
    password=forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={"class":"form-control"}),)


class VehicleForm(forms.Form):
        class Meta:
                model=Vehicle
                fields="__all__"
                Widget={
                        "title":forms.TextInput(attrs={"class":"form-control","placeholder":"Enter vehiclename"}),
                        "price":forms.NumberInput(attrs={"class":"form-control","placeholder":"Enter Price"}),
                        # "image":forms.ImageField(attrs={"class":"form-control","placeholder":"select image"}),
                        "category":forms.TextInput(attrs={"class":"form-control","placeholder":"Category"})
                }