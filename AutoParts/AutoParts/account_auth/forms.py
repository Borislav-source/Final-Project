from django import forms
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

UserModel = get_user_model()


class SignInForm(forms.Form):

    email = forms.EmailField(
        required='True',
        widget=forms.EmailInput(
            attrs={
                'class': "form-control",
            },
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': "form-control",
            }
        )
    )


class SignUpForm(UserCreationForm):
    email = forms.EmailInput(
        attrs={
            'class': 'form-control'
        })
    password = forms.PasswordInput(
        attrs={
            'class': 'form-control'
        }
    )

    class Meta:
        model = UserModel
        fields = ('email',)
