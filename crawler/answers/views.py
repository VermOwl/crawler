from django.shortcuts import render
import csv
from django.http import HttpResponse, request
from django.views.generic.base import View
from .models import Answer
from .serializers import AnswerSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status



# Create your views here.




class AnswerList(APIView):

    def get(self, request):
        questions = Answer.objects.all()
        serializer = AnswerSerializer(questions, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def export(request):
    
    response = HttpResponse(
        content_type='text/csv',
    )
    writer = csv.writer(response)
    writer.writerow(['Вопрос', 'Оборудование', 'Ответ', 'Замер', 'Дата'])
    for answer1 in Answer.objects.all().values_list('question', 'Equipment', 'answer', 'answerMeasurment', 'date'):
        writer.writerow(answer1)
    
    response['Content-Disposition'] = 'attachment; filename="answers.csv"'

    return response
