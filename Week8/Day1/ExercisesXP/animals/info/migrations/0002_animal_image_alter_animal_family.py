# Generated by Django 4.1.7 on 2023-03-07 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='animal',
            name='family',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.family'),
        ),
    ]