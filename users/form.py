from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite o nome do seu usuario'
            }
        ),
        label='Usuário'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Digite sua senha'
            }
        ),
        label='Senha'
    )