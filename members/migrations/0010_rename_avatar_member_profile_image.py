# Generated by Django 5.1.1 on 2024-12-10 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0009_alter_member_avatar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='avatar',
            new_name='profile_image',
        ),
    ]
