# Generated by Django 4.1.7 on 2023-03-09 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gifs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='gif',
            old_name='title',
            new_name='author',
        ),
        migrations.AlterField(
            model_name='gif',
            name='uploader_name',
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name='Category_model',
        ),
        migrations.AddField(
            model_name='gif',
            name='categories',
            field=models.ManyToManyField(related_name='gifs', to='gifs.category'),
        ),
    ]
