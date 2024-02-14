from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.conf import settings
from  django.views.generic.base import TemplateView
from django.contrib import messages
from .models import Appointment
from django.views.generic import ListView
from django.contrib import messages
import datetime
from django.template import Context
from django.template.loader import render_to_string, get_template
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
# def home(request):
#     return HttpResponse("It's working")


class DocTemplateView(TemplateView):
    template_name = "docindex.html"

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')


        email = EmailMessage(
            subject = f"{name}  from doctor family,",
            body=message,
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.EMAIL_HOST_USER],
            reply_to=[email]
            )
        email.send()
        return HttpResponse("Email sent successfully")



class AppointmentTemplateView(TemplateView):
    template_name = "appointment.html"

    def post(self, request):
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        message = request.POST.get("request")


        appointment = Appointment.objects.create(
            first_name = fname,
            last_name = lname,
            phone = mobile,
            request = message,
            )
        appointment.save()

        success_message = f"Thanks {fname} for making an appointment with us, we will email as soon as possible"
        messages.success(request, success_message)
        
        return redirect('appointment')




class ManageAppointmentTemplateView(ListView):
    template_name = "manage-appointments.html"
    model = Appointment
    context_object_name = "appointments"
    login_required = True
    paginate_by = 3

    def post(self, request ):  
        date = request.POST.get("date")
        appointment_id = request.POST.get("appointment-id")
        appointment = Appointment.objects.get(id=appointment_id)
        appointment.accepted = True
        appointment.accepted_date = datetime.datetime.now()
        appointment.save()

        data = {
        "fname":appointment.first_name,
        "date":date,
        }

        message = get_template('email.html').render(data)
        email  = EmailMessage(
            "About your appointment",
            message,
            settings.EMAIL_HOST_USER,
            [appointment.email],
            )

        email.content_subtype = "html"
        email.send()


        messages.add_message(request, messages.SUCCESS, f"You have accepted the appointment of {appointment.first_name}")
        return HttpResponseRedirect(request.path)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        
        # Get the page number from the request's GET parameters
        page_number = self.request.GET.get('page', 1)

        # Retrieve all appointments
        appointments = Appointment.objects.all()

        # Paginate the appointments
        paginator = Paginator(appointments, self.paginate_by)

        try:
            # Try to get the requested page
            appointments = paginator.page(page_number)
        except EmptyPage:
            # If the requested page is out of range, deliver the last page
            appointments = paginator.page(paginator.num_pages)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            appointments = paginator.page(1)

        context.update({
            "Title": "Manage Appointments",
            "appointments": appointments,
        })
        return context
