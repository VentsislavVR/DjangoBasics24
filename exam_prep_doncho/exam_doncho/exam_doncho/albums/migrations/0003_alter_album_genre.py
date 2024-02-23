# Generated by Django 5.0.2 on 2024-02-19 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0002_alter_album_artist_name_alter_album_image_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='genre',
            field=models.CharField(choices=[('Pop Music', 'Genre Pop'), ('Jazz Music', 'Genre Jazz'), ('Rock Music', 'Genre Rock'), ('Country Music', 'Genre Country'), ('R&B Music', 'Genre Rnb'), ('Dance Music', 'Genre Dance'), ('Hip Hop Music', 'Genre Hiphop'), ('Other', 'Genre Other')], max_length=30),
        ),
    ]