from django import forms
from cash_flow.models import RegisterModel

class RegisterFlows(forms.ModelForm):
    class Meta:
        model = RegisterModel
        fields = [
            'description',
            'nature',
            'type_cash',
            'value',
        ]