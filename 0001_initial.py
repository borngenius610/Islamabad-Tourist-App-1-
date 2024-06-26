# Generated by Django 5.0.6 on 2024-06-19 13:49

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='carbooking',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=225)),
                ('days', models.IntegerField()),
                ('phone', models.CharField(max_length=13)),
                ('numb', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='hotelbooking',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=225)),
                ('night', models.IntegerField()),
                ('phone', models.CharField(max_length=13)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=225)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=13)),
                ('slug', models.CharField(max_length=130)),
                ('timestamp', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='tourbooking',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=225)),
                ('person', models.IntegerField()),
                ('phone', models.CharField(max_length=13)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
