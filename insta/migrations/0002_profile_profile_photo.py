# Generated by Django 3.2.5 on 2021-07-13 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_photo',
            field=models.ImageField(default='SOME IMAGE', upload_to='profile/'),
        ),
    ]
