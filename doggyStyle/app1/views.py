from django.shortcuts import render
from rest_framework import generics
from .models import Breed
from .serializers import BreedSerializer

# Create your views here.

class BreedList(generics.ListCreateAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer

class BreedDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    