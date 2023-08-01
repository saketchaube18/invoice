# Generated by Django 4.2.3 on 2023-07-31 09:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='user',
            field=models.ForeignKey(default='admin', on_delete=django.db.models.deletion.DO_NOTHING, related_name='invoice', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]