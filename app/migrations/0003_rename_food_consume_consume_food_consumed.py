# Generated by Django 4.2.5 on 2023-12-02 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_consume'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consume',
            old_name='food_consume',
            new_name='food_consumed',
        ),
    ]
