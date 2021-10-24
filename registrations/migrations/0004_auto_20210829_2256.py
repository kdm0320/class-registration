# Generated by Django 3.2.6 on 2021-08-29 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0003_alter_registration_grade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='is_closed',
        ),
        migrations.AddField(
            model_name='registration',
            name='time',
            field=models.CharField(blank=True, max_length=8, verbose_name='강의시간'),
        ),
        migrations.AddField(
            model_name='registration',
            name='universe',
            field=models.CharField(choices=[('경영경제대학', '경영경제대학'), ('공과대학', '공과대학'), ('소프트웨어대학', '소프트웨어대학')], default='--선택--', max_length=10, verbose_name='대학'),
        ),
    ]