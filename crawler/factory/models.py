from django.db import models

class Factory(models.Model):
    factory_name = models.CharField('Название предприятия', max_length=100)

    def __str__(self):
        return self.factory_name

class Workshop(models.Model):
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE)
    workshop_name = models.CharField('Название цеха', max_length=200)

    def __str__(self):
        return self.workshop_name