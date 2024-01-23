# Generated by Django 5.0.1 on 2024-01-23 15:53

import django.db.models.deletion
import forms_basic.web.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='employee',
            name='first_name',
            field=models.CharField(max_length=35, validators=[forms_basic.web.models.non_empty_spaces]),
        ),
        migrations.AddField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='web.department'),
        ),
    ]
