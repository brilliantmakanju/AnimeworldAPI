# Generated by Django 3.2.13 on 2022-11-29 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=255)),
                ('season', models.CharField(max_length=255)),
                ('episode', models.CharField(max_length=255)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('published', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=255)),
                ('movieID', models.ForeignKey(default='4', on_delete=django.db.models.deletion.CASCADE, related_name='movvieID', to='movie.movies')),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='')),
                ('thumbnail', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=255)),
                ('seasonID', models.ForeignKey(default='2', on_delete=django.db.models.deletion.CASCADE, related_name='seaasonID', to='movie.season')),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
    ]
