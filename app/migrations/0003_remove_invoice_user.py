# Generated by Django 4.2.3 on 2023-07-31 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_invoice_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='user',
        ),
    ]
