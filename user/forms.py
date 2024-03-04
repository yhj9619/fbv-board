from django import forms
from django.contrib.auth.forms import UserCreationForm, ReadOnlyPasswordHashField

from .models import User

class UserForm(UserCreationForm):
    username = forms.CharField(label="아이디")
    password1 = forms.CharField(label="비밀번호")
    password2 = forms.CharField(label="비밀번호확인")
    last_name = forms.CharField(label="성")
    first_name = forms.CharField(label="이름")
    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = (
            "username",
            "last_name",
            "first_name",
            "password1",
            "password2",
            "email"
        )