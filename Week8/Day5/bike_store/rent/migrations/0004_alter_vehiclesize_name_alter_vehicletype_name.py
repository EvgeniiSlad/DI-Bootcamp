# Generated by Django 4.1.7 on 2023-03-13 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0003_alter_rental_rental_date_alter_rental_return_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehiclesize',
            name='name',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=2),
        ),
        migrations.AlterField(
            model_name='vehicletype',
            name='name',
            field=models.CharField(choices=[('C', 'City'), ('M', 'Mountain'), ('El', 'Electric')], max_length=2),
        ),
    ]
