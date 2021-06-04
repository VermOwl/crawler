from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.serializers import Serializer
from rest_framework.response import Response
from .models import Equipment
from .serializers import EquipmentSerializer
from rest_framework import status

class EquipmentList(APIView):

    def get(self, request):
        equipmnet = Equipment.objects.all()
        serializer = EquipmentSerializer(equipmnet, many = True)
        return Response(serializer.data)


    def post(self, request):
        serializer = EquipmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
