# Generated by Django 4.1.7 on 2023-02-24 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainmodel',
            name='clock_speed',
            field=models.DecimalField(decimal_places=1, max_digits=3, verbose_name='clock_speed'),
        ),
        migrations.AlterField(
            model_name='trainmodel',
            name='mobile_depth',
            field=models.DecimalField(decimal_places=1, max_digits=3, verbose_name='mobile_depth'),
        ),
    ]