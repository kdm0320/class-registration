# Generated by Django 3.2.7 on 2021-10-24 03:08

import basketLists.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classs', '0010_alter_class_people'),
        ('basketLists', '0013_auto_20211023_0034'),
    ]

    operations = [
        migrations.DeleteModel(
            name='List',
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_table', models.JSONField(default=basketLists.models.default_time_table_dict, null=True, verbose_name='시간표')),
                ('credits', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(23)], verbose_name='신청학점')),
                ('subjects', models.ManyToManyField(blank=True, to='classs.Class')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lists', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
