from django import forms
from .models import Author

class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password1 = forms.CharField(label='Пароль(еще раз)',widget=forms.PasswordInput)
    class Meta():
        model = Author
        fields = ['username', 'password', 'password1']