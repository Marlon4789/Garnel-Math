# Generated by Django 5.0 on 2024-01-06 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garnelmath', '0009_alter_feedback_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='feedback',
            field=models.TextField(unique=True, verbose_name='feedback'),
        ),
    ]
