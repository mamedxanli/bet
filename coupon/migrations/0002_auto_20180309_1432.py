# Generated by Django 2.0.3 on 2018-03-09 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='coupon_id',
            field=models.CharField(max_length=30, verbose_name='Coupon id'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='match5',
            field=models.CharField(max_length=50, verbose_name='Match 5'),
        ),
    ]
