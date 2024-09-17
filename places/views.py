from django.shortcuts import render
from rest_framework import viewsets

from .models import AccessibilityFeature, Place
from .serializers import AccessibilityFeatureSerializer, PlaceSerializer

# Create your views here.

class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer

class AccessibilityFeatureViewSet(viewsets.ModelViewSet):
    queryset = AccessibilityFeature.objects.all()
    serializer_class = AccessibilityFeatureSerializer
