# Generated by Django 4.0.5 on 2022-12-05 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('property_type', models.CharField(choices=[('S', 'sale'), ('R', 'rent')], max_length=10)),
                ('price', models.PositiveIntegerField()),
                ('area', models.DecimalField(decimal_places=2, max_digits=5)),
                ('beds_number', models.PositiveIntegerField()),
                ('baths_number', models.PositiveIntegerField()),
                ('garages_number', models.PositiveIntegerField()),
            ],
        ),
    ]
