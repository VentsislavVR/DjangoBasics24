# Generated by Django 5.0.2 on 2024-02-23 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='budget',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
