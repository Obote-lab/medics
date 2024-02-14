from rest_framework.routers import DefaultRouter
from .views import CompltViewSet


complt_router = DefaultRouter()
complt_router.register(r"completeHospitals", CompltViewSet)