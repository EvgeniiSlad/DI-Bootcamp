# Generated by Django 4.1.7 on 2023-03-22 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Realtot',
            new_name='Realtor',
        ),
    ]
