from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from django.http import JsonResponse
from geopy.distance import geodesic
from django.contrib import messages
import csv, io
# from tablib import Dataset
import json



from . models import( 
	Counties, 
	Sample,
	Sub_counties,
	Schools,
	Airports,
	Populated_Regions,
	WaterWays,
	Hospitals,
	Roads,
	Agriculture,
	ProtectedAreas,
	WetLands,


	# hb datasets
	HbAgric,
	Homa_Bay,
	H_B_HealthFacilities,
	Lakes,
	HbProtectedAreas,
	HbRivers,
	HbRoads,
	Hbschools,
	Soils,
	HbSubCounties,


	HomaBayHospCsv,
	CompltHospCsv,
	KephLevel,
	)


# from core.models import HomabayCsvHosp
# Create your views here.
def index(request):
	return render(request, 'index.html')

def county_datasets(request):
	counties = serialize('geojson',Counties.objects.all())
	return HttpResponse(counties, content_type='json')

def sample_datasets(request):
	samples = serialize('geojson', Sample.objects.all())
	return HttpResponse(samples, content_type = 'json')

def subcounties_datasets(request):
	subs = serialize('geojson', Sub_counties.objects.all())
	return HttpResponse(subs, content_type='json')

def schools_datasets(request):
	sch = serialize('geojson', Schools.objects.all())
	return HttpResponse(sch, content_type='json')

def airport_datasets(request):
	air = serialize('geojson',Airports.objects.all())
	return HttpResponse(air, content_type='json')

def popu_datasets(request):
	pop = serialize('geojson',Populated_Regions.objects.all())
	return HttpResponse(pop, content_type='json')
def waterway_datasets(request):
	water= serialize('geojson', WaterWays.objects.all())
	return HttpResponse(water, content_type='json')

def roads_datasets(request):
	rod = serialize('geojson',Roads.objects.all())
	return HttpResponse(rod, content_type='json')

def agric_datasets(request):
	agric = serialize('geojson',Agriculture.objects.all())
	return HttpResponse(agric, content_type='json')

def protect_datasets(request):
	prot = serialize('geojson',ProtectedAreas.objects.all())
	return HttpResponse(prot, content_type='json')

def wetlands_datasets(request):
	wet = serialize('geojson', WetLands.objects.all())
	return HttpResponse(wet, content_type='json')

def hospitals_datasets(request):
	hosi = serialize('geojson',Hospitals.objects.all())
	return HttpResponse(hosi, content_type='json')


# hb views
def homabay(request):
	return render(request, 'homabay.html')

def hbagric_datasets(request):
	agric = serialize('geojson', HbAgric.objects.all())
	return HttpResponse(agric, content_type='json')

def hbcounty_datasets(request):
	hb = serialize('geojson', Homa_Bay.objects.all())
	return HttpResponse(hb, content_type='json')

def hbhosp_datasets(request):
	hos = serialize('geojson',H_B_HealthFacilities.objects.all())
	return HttpResponse(hos, content_type='json')

def lakes_datasets(request):
	lakes = serialize('geojson', Lakes.objects.all())
	return HttpResponse(lakes, content_type='json')

def hbpro_datasets(request):
	pro = serialize('geojson', HbProtectedAreas.objects.all())
	return HttpResponse(pro, content_type='json')

def hbrivers_datasets(request):
	riv = serialize('geojson', HbRivers.objects.all())
	return HttpResponse(riv, content_type='json')

def hbro_datasets(request):
	ro = serialize('geojson', HbRoads.objects.all())
	return HttpResponse(ro, content_type='json')

def hbsch_datasets(request):
	sch = serialize('geojson', Hbschools.objects.all())
	return HttpResponse(sch, content_type='json')

def soils_datasets(request):
	so = serialize('geojson', Soils.objects.all())
	return HttpResponse(so, content_type='json')

def hbsubco_datasets(request):
	sub = serialize('geojson', HbSubCounties.objects.all())
	return HttpResponse(sub, content_type='json')



	# routing
def routing(request):
	hospitals = list(CompltHospCsv.objects.values('latitude','longitude','facility_n','Keph_level','Facility_type','Open_whole_day','Open_late_night','Open_weekends','Open_public_holidays'))
	context = {"hospitals":hospitals}
	return render(request, 'routing.html', context)






def nearest_healthfacility(request):
    latitude = float(request.GET.get("latitude"))
    longitude = float(request.GET.get("longitude"))

    user_location = (latitude, longitude)
    hospital_distances = {}

    for hospital in CompltHospCsv.objects.all():
        hospital_location = (hospital.latitude, hospital.longitude)

        # calculate the distance between the user's location and the hospitals
        distance = geodesic(user_location, hospital_location).km
        hospital_distances[distance] = {
            'coordinates': hospital_location,
            'facility_n': hospital.facility_n,
            'Keph_level': hospital.Keph_level,
            'Facility_type': hospital.Facility_type,
            'Open_whole_day': hospital.Open_whole_day,
            'Open_late_night': hospital.Open_late_night,
            'Open_weekends': hospital.Open_weekends,
            'Open_public_holidays': hospital.Open_public_holidays,
        }

    min_distance = min(hospital_distances)
    nearest_hospital_info = hospital_distances[min_distance]

    return JsonResponse({
        'coordinates': nearest_hospital_info['coordinates'],
        'distance': min_distance,
        'facility_n': nearest_hospital_info['facility_n'],
        'Keph_level': nearest_hospital_info['Keph_level'],
        'Facility_type': nearest_hospital_info['Facility_type'],
        'Open_whole_day': nearest_hospital_info['Open_whole_day'],
        'Open_late_night': nearest_hospital_info['Open_late_night'],
        'Open_weekends': nearest_hospital_info['Open_weekends'],
        'Open_public_holidays': nearest_hospital_info['Open_public_holidays'],
    })



def hbbase(request):
	return render(request, 'homabay_base.html')
def hbroads_map(request):
	return render(request, 'homabay_roads.html')
def hbschools_map(request):
	return render(request, 'homabay_schools.html')
def hbsubcounties_map(request):
	return render(request, 'homabay_subcounties.html')
def hbhealthfacilities_map(request):
	return render(request, 'homabay_healthfacilities.html')

def realtime_locator(request):
    return render(request, 'realtime_locator.html')

def flight(request):
	hosis = list(CompltHospCsv.objects.values('latitude','longitude','facility_n','Keph_level','Facility_type','Open_whole_day','Open_late_night','Open_weekends','Open_public_holidays'))
	context = {"hosis": hosis}
	return render(request, 'directflight.html', context)


	


def nearest_hosi(request):
    latitude = float(request.GET.get('latitude'))
    longitude = float(request.GET.get('longitude'))

    user_location = latitude, longitude
    hosi_distances = {}

    for hosy in CompltHospCsv.objects.all():
        hosy_location = hosy.latitude, hosy.longitude

        # calculate the distances from the user to hosys
        distance = geodesic(user_location, hosy_location).km
        hosi_distances[distance] = {
            'coordinates': hosy_location,
            'facility_n': hosy.facility_n,
            'Keph_level': hosy.Keph_level,
            'Facility_type': hosy.Facility_type,
            'Open_whole_day': hosy.Open_whole_day,
            'Open_late_night': hosy.Open_late_night,
            'Open_weekends': hosy.Open_weekends,
            'Open_public_holidays': hosy.Open_public_holidays,
        }

    min_hosy_distance = min(hosi_distances)
    nearest_hosi_info = hosi_distances[min_hosy_distance]

    return JsonResponse({
        'coordinates': nearest_hosi_info['coordinates'],
        'distance': min_hosy_distance,
        'facility_n': nearest_hosi_info['facility_n'],
        'Keph_level': nearest_hosi_info['Keph_level'],
        'Facility_type': nearest_hosi_info['Facility_type'],
        'Open_whole_day': nearest_hosi_info['Open_whole_day'],
        'Open_late_night': nearest_hosi_info['Open_late_night'],
        'Open_weekends': nearest_hosi_info['Open_weekends'],
        'Open_public_holidays': nearest_hosi_info['Open_public_holidays'],
    })


def Allroutes(request):
	return render(request, 'allrouting.html')


def Osiptende(request):
	return render(request, 'osiptende.html')

def LocViable(request):
	return render(request, 'realtime_loc_viable.html')
