# Generated by Django 5.0 on 2024-01-06 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garnelmath', '0004_rename_subscribe_subscription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='email',
            field=models.EmailField(max_length=100, unique=True, verbose_name='email'),
        ),
    ]