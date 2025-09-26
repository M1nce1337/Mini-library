from django import forms
from django.contrib.auth import get_user_model


class LoginUserForm(forms.Form):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-input'}))

class RegisterUserForm(forms.Form):
    username = forms.CharField(label="Логин", widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'password']
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия'
        }

    def clean_name(self):
        name = self.cleaned_data['username']

        if get_user_model().objects.filter(username=name).exists():
            raise forms.ValidationError('Такое имя уже существует!')

        return name

