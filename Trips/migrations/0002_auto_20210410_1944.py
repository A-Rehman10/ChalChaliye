# Generated by Django 3.1.3 on 2021-04-10 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Trips', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='discount',
            field=models.CharField(max_length=32),
        ),
    ]
