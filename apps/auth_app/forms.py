from django import forms


class SignUpForm(forms.Form):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100, required=True)
    second_name = forms.CharField(max_length=100, required=False)
    password = forms.CharField(max_length=10, widget=forms.PasswordInput())
    confirm_password = forms.CharField(
        max_length=10, widget=forms.PasswordInput())


class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(max_length=10, widget=forms.PasswordInput())
