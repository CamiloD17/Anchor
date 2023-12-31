# Generated by Django 4.2.7 on 2023-11-17 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_userprofile_following_follower'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follower',
            name='user_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower_profile', to='users.userprofile'),
        ),
    ]
