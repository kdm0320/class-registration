# Generated by Django 3.2.7 on 2021-10-14 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basketLists', '0010_alter_list_time_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='time_table',
            field=models.JSONField(default={'금': [], '목': [], '수': [], '월': [], '화': []}, null=True, verbose_name='시간표'),
        ),
    ]
