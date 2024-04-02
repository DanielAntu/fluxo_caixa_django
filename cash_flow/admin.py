from django.contrib import admin
from . import models

@admin.register(models.RegisterModel)
class RegisterAdmin(admin.ModelAdmin):
    ordering= '-created_at',
    list_display = ['description', 'value', 'nature', 'type_cash', 'created_at']
    search_fields = ['description', 'value', 'nature', 'type_cash', 'created_at']
    list_editable = ['value', 'nature', 'type_cash']