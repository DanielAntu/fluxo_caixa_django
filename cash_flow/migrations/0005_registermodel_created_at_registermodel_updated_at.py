# Generated by Django 5.0.3 on 2024-03-19 13:53

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cash_flow', '0004_alter_registermodel_type_cash'),
    ]

    operations = [
        migrations.AddField(
            model_name='registermodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registermodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
