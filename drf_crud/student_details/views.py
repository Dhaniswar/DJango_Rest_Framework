from django.shortcuts import render
from django.http import HttpResponce, JsonResponce
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.responce import Responce
from rest_framework import status
from rest_framework.http import Http404
from .models import Student
from .serializers import StudentSerializer



class StudentList(APIView):
    
    def get(self, request):
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return Responce(serializer.data)