# Generated by Django 5.0.3 on 2024-03-19 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cash_flow', '0002_registermodel_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registermodel',
            name='description',
            field=models.CharField(max_length=150),
        ),
    ]