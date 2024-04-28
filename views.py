

# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import InfoSerializer
from .models import Informacion

class InformacionAPIView(generics.RetrieveAPIView):
    lookup_field="codigo"
    queryset=Informacion.objects.all()
    serializer_class=InfoSerializer

class InformacionDescripcionAPIView(generics.ListAPIView):
    serializer_class = InfoSerializer

    def get_queryset(self):
        descripcion = self.kwargs['descripcion']
       
        queryset = Informacion.objects.filter(descripcion__icontains=descripcion)
        return queryset

class TodasAPIView(generics.ListAPIView):
    queryset=Informacion.objects.all()
    serializer_class=InfoSerializer   