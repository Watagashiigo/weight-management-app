from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="ユーザー名",
        widget=forms.TextInput(attrs={"placeholder": "Username"})
    )
    password = forms.CharField(
        label="パスワード",
        widget=forms.PasswordInput(attrs={"placeholder": "Password"})
    )


class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        label="パスワード",
        widget=forms.PasswordInput(attrs={"placeholder": "Password"})
    )
    password_confirm = forms.CharField(
        label="パスワード確認",
        widget=forms.PasswordInput(attrs={"placeholder": "Confirm Password"})
    )

    class Meta:
        model = User
        fields = ["username", "email", "password"]
        labels = {
            "username": "ユーザー名",
            "email": "メールアドレス",
        }
        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "Username"}),
            "email": forms.EmailInput(attrs={"placeholder": "Email"}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise forms.ValidationError("パスワードが一致しません。")

        return cleaned_data
