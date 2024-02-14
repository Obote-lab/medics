from rest_framework import viewsets
from .serializers import CompltHospSerializer
from ..models import CompltHospCsv


class CompltViewSet(viewsets.ModelViewSet):
	queryset 			= CompltHospCsv.objects.all()
	serializer_class 	= CompltHospSerializer