from django.urls import path
from .views import DocTemplateView,AppointmentTemplateView,ManageAppointmentTemplateView



urlpatterns = [
    path("doctor-side/", DocTemplateView.as_view(), name='home'),
    path("make-an-appointment/", AppointmentTemplateView.as_view(), name='appointment'),
    path("manage-appointments/", ManageAppointmentTemplateView.as_view(), name='manage'),
]