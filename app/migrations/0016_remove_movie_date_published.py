# Generated by Django 4.1.7 on 2023-03-22 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_reservation_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='date_published',
        ),
    ]
