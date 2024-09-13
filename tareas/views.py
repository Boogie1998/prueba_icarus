from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Tarea
from .serializers import TareaSerializer


class ListaTareasApiView(ListCreateAPIView):

    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer


class TareasApiView(RetrieveUpdateDestroyAPIView):

    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer