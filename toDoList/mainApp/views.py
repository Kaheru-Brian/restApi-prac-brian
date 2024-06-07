from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .models import *

# Create your views here.
#in the rest api we follow CRUD operatioms

class ListTodo(generics.ListAPIView): #read
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    
class DetailTodo(generics.RetrieveAPIView): #update
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    
class CreateTodo(generics.CreateAPIView): #create
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    
class DeleteTodo(generics.DestroyAPIView): #Delete
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer