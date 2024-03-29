# Generated by Django 5.0.2 on 2024-02-13 07:47

import cbv_advanced.web.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='todo',
            name='slug',
            field=models.SlugField(default=cbv_advanced.web.models.generate_slug, editable=False, max_length=28),
        ),
        migrations.AddField(
            model_name='todo',
            name='tenant',
            field=models.CharField(blank=True, default=None, max_length=16, null=True),
        ),
    ]
