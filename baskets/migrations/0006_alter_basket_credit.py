# Generated by Django 3.2.6 on 2021-08-31 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baskets', '0005_alter_basket_credit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='credit',
            field=models.CharField(blank=True, max_length=2, verbose_name='학점'),
        ),
    ]
