from factory.serializers import FactorySerializer
from rest_framework.views import APIView
from rest_framework.serializers import Serializer
from rest_framework.response import Response
from .models import Factory, Workshop
from .serializers import FactorySerializer, WorkshopSerializer
from rest_framework import status


class FactoryList(APIView):

    def get(self, request):
        factories = Factory.objects.all()
        serializer = FactorySerializer(factories, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FactorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WorkShopList(APIView):

    def get(self, request):
        workshops = Workshop.objects.all()
        serializer = WorkshopSerializer(workshops, many = True)
        return Response(serializer.data)