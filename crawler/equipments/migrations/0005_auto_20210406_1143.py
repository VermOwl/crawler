# Generated by Django 3.1.7 on 2021-04-06 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
        ('equipments', '0004_equipment_questionsmeasuring'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='nfc_mark',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='NFC Мека'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='questions',
            field=models.ManyToManyField(blank=True, null=True, to='questions.QuestionYN', verbose_name='Название вопроса'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='questionsMeasuring',
            field=models.ManyToManyField(blank=True, null=True, to='questions.QuestionMeasuring', verbose_name='Название вопроса замера'),
        ),
    ]
