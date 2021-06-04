from django.db import models


# Create your models here.
class Answer(models.Model):

    class Answer(models.IntegerChoices):
        NO = 0
        YES = 1
        UNKNOW = 2

    question = models.ForeignKey("questions.QuestionMeasuring", on_delete=models.CASCADE)
    Equipment = models.ForeignKey("equipments.Equipment", on_delete=models.CASCADE, default=0)
    answer = models.IntegerField(choices=Answer.choices, default=2, blank=True, null=True)
    answerMeasurment = models.IntegerField(verbose_name="Замер", blank=True, null=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        displayedName = str(self.question) + " " + str(self.Equipment)
        return displayedName
