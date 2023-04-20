from django.shortcuts import render
from .serializers import TestSerializer 
from rest_framework import viewsets      
from .models import TestModel

# Create your views here.               

class TestView(viewsets.ModelViewSet):  
    serializer_class = TestSerializer   
    queryset = TestModel.objects.all()     