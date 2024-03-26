from django import forms
from cash_flow.models import RegisterModel
import re

class RegisterFlows(forms.ModelForm):
    description = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Digite a descrição'
        })
    )

    value = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Digite o valor',
            'class': 'value_rs'
        })
    )

    class Meta:
        model = RegisterModel
        fields = [
            'description',
            'nature',
            'type_cash',
            'value',
        ]

    def clean_value(self):
        data = self.cleaned_data.get('value', '')
        regex = r'^[0-9]+([,][0-9]{1,2}?$)'

        if not re.match(regex, data):
            raise forms.ValidationError('Por favor insira um número válido')
        
        return data