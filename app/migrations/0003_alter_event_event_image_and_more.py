# Generated by Django 4.1.7 on 2023-03-02 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_image',
            field=models.ImageField(upload_to='images/events/'),
        ),
        migrations.AlterField(
            model_name='partnerbrand',
            name='brand_image',
            field=models.ImageField(upload_to='images/partner_brands/'),
        ),
    ]
