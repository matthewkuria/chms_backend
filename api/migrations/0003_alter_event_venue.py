# Generated by Django 5.1.1 on 2024-12-09 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_inventory_issued_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='venue',
            field=models.CharField(default='NCCI, Lanet.', max_length=100),
        ),
    ]