# Generated by Django 5.0.6 on 2024-06-19 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carbooking',
            name='numb',
            field=models.IntegerField(default=1),
        ),
    ]
