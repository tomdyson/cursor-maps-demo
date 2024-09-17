from rest_framework import serializers

from .models import AccessibilityFeature, Place


class AccessibilityFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessibilityFeature
        fields = ['id', 'name', 'description']

class PlaceSerializer(serializers.ModelSerializer):
    accessibility_features = AccessibilityFeatureSerializer(many=True, read_only=True)

    class Meta:
        model = Place
        fields = ['id', 'name', 'description', 'address', 'latitude', 'longitude', 'category', 'accessibility_features']