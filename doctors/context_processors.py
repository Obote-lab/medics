from .models import Appointment


def get_notification(request):
	count = Appointment.objects.filter(accepted = True).count
	data = {
			"count":count
	}
	return data