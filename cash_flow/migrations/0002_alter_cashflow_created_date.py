# Generated by Django 5.2 on 2025-04-11 14:07

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cash_flow', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashflow',
            name='created_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата создания'),
        ),
    ]
