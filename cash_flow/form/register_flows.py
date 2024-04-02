from django import forms
from django.core.exceptions import ValidationError
from cash_flow.models import RegisterModel
import re

class RegisterFlows(forms.ModelForm):
    description = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Digite a descrição'
        }),
        label='Descrição',
    )

    value = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Digite o valor',
            'class': 'value_rs'
        }),
        label='Valor'
    )

    class Meta:
        model = RegisterModel
        fields = [
            'description',
            'nature',
            'type_cash',
            'value',
        ]

        labels = {
            'nature': 'Natureza',
            'type_cash': 'Tipo',
        }


    def clean_value(self):
        data = self.cleaned_data.get('value', '')
        regex = r'^[0-9]+([,][0-9]{1,2}?$)'

        if not re.match(regex, data):
            raise forms.ValidationError('Por favor insira um número válido')
        
        return data
    
    def clean(self):
        cleaned_data = super().clean()
        nature = cleaned_data.get('nature')
        type_cash = cleaned_data.get('type_cash')

        if nature == 'output' and type_cash != '':
            raise ValidationError({
                'nature': ValidationError(
                    'Apenas selecione o tipo quando a natureza for igual a entrada',
                    code='invalid'
                )
            })
        elif nature == 'entry' and type_cash == '':
            raise ValidationError({
                'nature': ValidationError(
                    'Selecione o tipo do pagamento',
                    code='invalid'
                )
            })