# Generated by Django 3.1.7 on 2021-04-05 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='current',
            field=models.IntegerField(null=True, verbose_name='Ток'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='voltage',
            field=models.IntegerField(null=True, verbose_name='Напряжение'),
        ),
    ]