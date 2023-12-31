# Generated by Django 5.0 on 2023-12-28 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('description', models.CharField(max_length=300, verbose_name='description')),
                ('content', models.TextField(verbose_name='content')),
                ('image', models.URLField(verbose_name='image')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='date_created')),
            ],
        ),
    ]
