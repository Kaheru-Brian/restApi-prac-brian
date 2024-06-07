from django.shortcuts import render
from rest_framework import generics
from .models import toDo
from .serializers import toDoSerializer


# Create your views here.

class TodoListView(generics.ListCreateAPIView):
    queryset = toDo.objects.all()
    serializer_class = toDoSerializer


class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = toDo.objects.all()
    serializer_class = toDoSerializer