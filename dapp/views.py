from django.shortcuts import render

# Create your views here.
from .serializers import TodoSerializer
from .models import Todo
from rest_framework import viewsets

class TodoView(viewsets.ModelViewSet):
    serializer_class=TodoSerializer
    queryset=Todo.objects.all()
