# Generated by Django 4.0.5 on 2022-12-06 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_alter_property_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='image',
            field=models.ImageField(null=True, upload_to='property/'),
        ),
    ]
