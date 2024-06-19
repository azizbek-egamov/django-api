from django.shortcuts import render
from main.models import Kitob
from rest_framework import generics
from .serializers import KitoblarSerializer

# Create your views here.

class KitoblarViews(generics.ListAPIView):
    queryset = Kitob.objects.all()
    serializer_class = KitoblarSerializer
    
class kitoblarCreateView(generics.CreateAPIView):
    queryset = Kitob.objects.all()
    serializer_class = KitoblarSerializer
    
class KitoblarListCreateView(generics.ListCreateAPIView):
    queryset = Kitob.objects.all()
    serializer_class = KitoblarSerializer
    
class KitoblarDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Kitob.objects.all()
    serializer_class = KitoblarSerializer
    
class KitoblarUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Kitob.objects.all()
    serializer_class = KitoblarSerializer