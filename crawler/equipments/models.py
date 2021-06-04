from django.db import models
from django.db.models.deletion import CASCADE
from factory.models import Factory

# Create your models here.
class Equipment(models.Model):
    equipment_name = models.CharField(verbose_name='Название оборудования', max_length=100)
    factory = models.ForeignKey(to=Factory, verbose_name="Предприятие", on_delete=CASCADE, null=True)
    voltage = models.IntegerField(verbose_name='Напряжение', blank=True, null=True)
    current = models.IntegerField(verbose_name='Ток', blank=True, null=True)
    nfc_mark = models.CharField(verbose_name="NFC Мека", max_length=50, blank=True, null=True)

    def __str__(self):
        return self.equipment_name