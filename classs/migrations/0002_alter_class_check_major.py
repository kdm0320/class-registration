# Generated by Django 3.2.6 on 2021-08-17 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='check_major',
            field=models.CharField(choices=[('전공', '전공'), ('교양', '교양')], default='--선택--', max_length=10, verbose_name='이수구분'),
        ),
    ]
