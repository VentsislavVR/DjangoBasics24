# Generated by Django 5.0.2 on 2024-02-19 13:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_alter_plant_plant_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='plant',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='web.profile'),
            preserve_default=False,
        ),
    ]