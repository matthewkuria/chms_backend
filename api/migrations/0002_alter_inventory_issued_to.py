# Generated by Django 5.1.1 on 2024-10-24 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='issued_to',
            field=models.CharField(choices=[('bible school', 'Bible School'), ('church', 'Church')], default='ncci', max_length=50),
        ),
    ]
