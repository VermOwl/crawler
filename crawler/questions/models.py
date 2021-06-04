from django.db import models


class QuestionMeasuring(models.Model):

    qeustion_name = models.CharField('Название замеров', max_length=100)
    voltage = models.IntegerField('Допустимое отклонение от нормы, %', blank=True, null=True)
   
        
    def __str__(self):
        return self.qeustion_name