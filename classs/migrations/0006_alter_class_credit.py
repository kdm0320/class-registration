# Generated by Django 3.2.6 on 2021-08-30 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classs', '0005_alter_class_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='credit',
            field=models.CharField(blank=True, choices=[(0.5, '0.5'), (1, '1'), (2, '2'), (3, '3')], max_length=2, verbose_name='학점'),
        ),
    ]
