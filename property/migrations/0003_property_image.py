# Generated by Django 4.0.5 on 2022-12-06 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_alter_property_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='image',
            field=models.ImageField(default=0, upload_to='property/,'),
        ),
    ]
