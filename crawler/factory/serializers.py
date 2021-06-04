from rest_framework import serializers
from .models import Factory, Workshop

class FactorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Factory
        fields = '__all__'

class WorkshopSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Workshop
        fields = '__all__'

