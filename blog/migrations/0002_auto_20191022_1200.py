# Generated by Django 2.2.6 on 2019-10-22 03:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='published_data',
            new_name='published_date',
        ),
        migrations.AlterField(
            model_name='post',
            name='created_data',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
