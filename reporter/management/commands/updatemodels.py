from django.core.management.base import BaseCommand
import pandas as pd
from reporter.models import HomaBayHospCsv
class Command(BaseCommand):
	help = "Import Booms"

	def add_arguments(self, parser):
		pass

	def handle(self, *args, **options): 
		# Database Connections
		df = pd.read_csv("HealthFacilities.csv")

		for Object_id,Facility_n,Categories,Owner,County,Sub_county,Division,Location,Sub_location,Constituency,Nearest_to,Latitude,Longitude in zip(df.object_id,df.facility_n,df.categories,df.owner,df.county,df.sub_county,df.division,df.location,df.sub_location,df.constituency,df.nearest_to,df.latitude,df.longitude):

			models = HomaBayHospCsv(
						object_id = Object_id,
						facility_n=Facility_n,
						categories=Categories,
						owner=Owner,
						county=County,
						sub_county=Sub_county,
						division=Division,
						location=Location,
						sub_location=Sub_location,
						constituency=Constituency,
						nearest_to=Nearest_to,
						latitude=Latitude,
						longitude=Longitude)
			models.save()