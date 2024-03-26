from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class RegisterModel(models.Model):
    class Meta:
        verbose_name = 'Registro de caixa'
        verbose_name_plural = 'Registros'

    nature_dict = {
        'entry': 'Entrada',
        'output': 'Saida'
    }

    type_dict = {
        'cc': 'Cartão de Crédito',
        'cd': 'Cartão de Débito',
        'din': 'Dinheiro',
        'pix': 'Pix'
    }

    description = models.CharField(max_length=150, blank=False)
    nature = models.CharField(max_length=8, choices=nature_dict, blank=False, default=nature_dict['entry'])
    type_cash = models.CharField(max_length=8, choices=type_dict, blank=True)
    value = models.CharField(max_length=10, blank=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.description