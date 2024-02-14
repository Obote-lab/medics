from rest_framework.routers import DefaultRouter
from django.urls import path, include
from reporter.api.urls import complt_router


router = DefaultRouter()

# app1
# app2
# hospitals

router.registry.extend(complt_router.registry)


urlpatterns = [
	path('', include(router.urls)),
]