# Generated by Django 3.1.7 on 2021-04-06 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('questions', '0003_remove_questionmeasuring_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.IntegerField(blank=True, choices=[(0, 'No'), (1, 'Yes'), (2, 'Unknow')], default=2, null=True)),
                ('answerMeasurment', models.IntegerField(blank=True, null=True, verbose_name='Замер')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.questionmeasuring')),
            ],
        ),
    ]