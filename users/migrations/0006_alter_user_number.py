# Generated by Django 3.2.7 on 2021-09-26 03:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='number',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(99999999)], verbose_name='학번'),
        ),
    ]