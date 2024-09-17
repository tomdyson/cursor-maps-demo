from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AccessibilityFeatureViewSet, PlaceViewSet

router = DefaultRouter()
router.register(r'places', PlaceViewSet)
router.register(r'accessibility-features', AccessibilityFeatureViewSet)

urlpatterns = [
    path('', include(router.urls)),
]