from django.contrib import admin

from .models import AccessibilityFeature, Place

# Register your models here.

admin.site.register(Place)
admin.site.register(AccessibilityFeature)
