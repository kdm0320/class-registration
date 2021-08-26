# Generated by Django 3.2.6 on 2021-08-24 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0002_alter_registration_check_major'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='grade',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('공통', '공통')], default='--선택--', max_length=2, verbose_name='학년'),
        ),
    ]
