# Generated by Django 3.2.7 on 2021-10-17 15:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0008_registration_time_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='credits',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(23)], verbose_name='신청학점'),
        ),
    ]
