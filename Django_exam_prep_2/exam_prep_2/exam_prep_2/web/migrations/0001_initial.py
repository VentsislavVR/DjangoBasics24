# Generated by Django 5.0.2 on 2024-02-19 12:14

import django.core.validators
import exam_prep_2.web.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plant_type', models.CharField(choices=[], max_length=14)),
                ('name', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2), exam_prep_2.web.validators.validate_plant_name])),
                ('image_url', models.URLField()),
                ('description', models.TextField()),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(2)])),
                ('first_name', models.CharField(max_length=20, validators=[exam_prep_2.web.validators.validate_profile_name])),
                ('last_name', models.CharField(max_length=20, validators=[exam_prep_2.web.validators.validate_profile_name])),
                ('profile_picture', models.URLField(blank=True, null=True)),
            ],
        ),
    ]