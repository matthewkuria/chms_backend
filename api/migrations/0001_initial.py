# Generated by Django 5.1.1 on 2024-10-23 07:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('members', '0004_member_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('doe', models.DateField(blank=True, default=None, null=True)),
                ('description', models.TextField()),
                ('event_image', models.ImageField(default='default.jpg', upload_to='images/')),
                ('venue', models.CharField(default='NCCI,Lanet.', max_length=100)),
                ('coordinated_by', models.CharField(default='pst. Sharon', max_length=100)),
                ('budget', models.CharField(blank=True, max_length=255, null=True)),
                ('dept', models.CharField(choices=[('Protocol', 'Protocol'), ('worship', 'Praise & Worship'), ('prayers', 'Prayer & Intercessory'), ('media', 'Media & Publicity'), ('pastoral', 'Pastoral'), ('evangelism', 'Evangelism'), ('discipleship', 'Discipleship'), ('youth', 'Youth'), ('children', 'Children'), ('men', 'Men'), ('women', 'Women'), ('mercy', 'Mercy Team'), ('church_care', 'Church Care'), ('missions', 'Missions')], default='mercy', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.CharField(default=1, max_length=255)),
                ('serial_number', models.CharField(blank=True, max_length=100, null=True)),
                ('item_name', models.CharField(max_length=30)),
                ('issued_to', models.CharField(choices=[('bible school', 'Bible School'), ('ncci', 'Church')], default='ncci', max_length=50)),
                ('description', models.CharField(max_length=255)),
                ('date_received', models.DateField(blank=True, default=None, null=True)),
                ('current_condition', models.CharField(choices=[('good', 'Good'), ('faulty', 'Faulty'), ('poor', 'Poor')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='News', max_length=255)),
                ('date_posted', models.DateField(auto_now=True)),
                ('by', models.CharField(default='church admin', max_length=20, null=True)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_present', models.CharField(default=0, max_length=10)),
                ('doa', models.DateField(blank=True, default=None, null=True, unique=True)),
                ('present_status', models.CharField(choices=[('present', 'Present'), ('absent', 'Absent')], max_length=10)),
            ],
            options={
                'unique_together': {('total_present', 'doa')},
            },
        ),
        migrations.CreateModel(
            name='ChurchLeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=100, null=True)),
                ('date_appointed', models.DateField(blank=True, default=None, null=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.member')),
            ],
        ),
    ]
