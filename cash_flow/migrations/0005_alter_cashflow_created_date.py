# Generated by Django 5.2 on 2025-04-14 07:46

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cash_flow', '0004_alter_cashflow_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cashflow',
            name='created_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, verbose_name='Дата создания'),
        ),
    ]
