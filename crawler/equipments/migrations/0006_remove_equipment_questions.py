# Generated by Django 3.1.7 on 2021-04-06 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipments', '0005_auto_20210406_1143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipment',
            name='questions',
        ),
    ]
