
from rest_framework.views import APIView
from rest_framework.serializers import Serializer
from rest_framework.response import Response
from .models import QuestionMeasuring
from .serializers import QuestionMeasuringSerializer
from rest_framework import status

class QuestionMeasuringfList(APIView):

    def get(self, request):
        questions = QuestionMeasuring.objects.all()
        serializer = QuestionMeasuringSerializer(questions, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = QuestionMeasuringSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
