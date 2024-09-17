from django.db import models

# Create your models here.

class AccessibilityFeature(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Place(models.Model):
    CATEGORY_CHOICES = [
        ('SHOP', 'Shop'),
        ('RESTAURANT', 'Restaurant'),
    ]

    name = models.CharField(max_length=200)
    description = models.TextField()
    address = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    accessibility_features = models.ManyToManyField(AccessibilityFeature)

    def __str__(self):
        return self.name
