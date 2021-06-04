from rest_framework import serializers
from .models import QuestionMeasuring

class QuestionMeasuringSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionMeasuring
        fields = '__all__'
