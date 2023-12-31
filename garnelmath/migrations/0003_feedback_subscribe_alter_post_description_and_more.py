# Generated by Django 5.0 on 2024-01-05 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garnelmath', '0002_alter_post_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField(blank=True, verbose_name='feedback')),
                ('date', models.DateField(auto_now_add=True, verbose_name='date')),
            ],
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('date', models.DateField(auto_now_add=True, verbose_name='date')),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(blank=True, max_length=300, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.URLField(blank=True),
        ),
    ]
