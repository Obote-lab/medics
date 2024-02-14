from . import views 
from django.urls import path,include
from django.contrib import admin

urlpatterns = [
			#nation wide urls
		path('kenya/' ,views.index, name='kenyan_map'),
		path('county_data/',views.county_datasets, name='county'),
		path('sample_data/',views.sample_datasets, name='sample'),
		path('subcounties_data/', views.subcounties_datasets, name='sub_county'),
		path('schools_data/',views.schools_datasets, name = 'schools'),
		path('airport_data/',views.airport_datasets, name='airports'),
		path('popu_data/',views.popu_datasets,name='populated_regions'),
		path('waterway_data/', views.waterway_datasets, name='waterways'),
		path('hospitals_data/',views.hospitals_datasets, name='health_facilities'),
		path('roads_data/', views.roads_datasets, name='roads'),
		path('agric_data/',views.agric_datasets, name='agricultural_areas'),
		path('protect_data/',views.protect_datasets,name='protected_areas'),
		path('wetlands_data/', views.wetlands_datasets,name='wetlands'),


		# HOMA BAY DATA URLS
		path('homabay/', views.homabay, name='homabay_map'),
		path('hbagric_data/', views.hbagric_datasets, name='hb_agric'),
		path('hbcounty_data/', views.hbcounty_datasets, name='Hb_County'),
		path('hbhospitals_data/', views.hbhosp_datasets, name='Hb_Hosp'),
		path('lakes_data/', views.lakes_datasets, name='L.Victoria'),
		path('hbprotectedareas_data/', views.hbpro_datasets, name='Hb_ProtectedAreas'),
		path('hbrivers_data/', views.hbrivers_datasets, name='Hb_rivers'),
		path('hbroads_data/', views.hbro_datasets, name='Hb_Roads'),
		path('hbschools_data/', views.hbsch_datasets, name='Hb_Schools'),
		path('soils_data/', views.soils_datasets, name='Soils'),
		path('hbsubcounties_data/', views.hbsubco_datasets, name='Hb_subcounties'),

		path('routing/', views.routing, name='routes'),
		path("get-nearest-healthfacility/", views.nearest_healthfacility),
		path("get-nearest-hosi/", views.nearest_hosi),
		
		path('hbbase/', views.hbbase, name='Homabay_base'),
		path('hbroads_map/', views.hbroads_map, name='Homabay_roads'),
		path('hbschools_map/', views.hbschools_map, name='Homabay_schools'),
		path('hbsubcounties_map/', views.hbsubcounties_map, name='Homabay_subcounties'),
		path('hbhealthfacilities_map/', views.hbhealthfacilities_map, name='Homabay_healthfacilities'),
		path('realtime_locator/', views.realtime_locator, name='realtime_locator'),
		path('flight/', views.flight, name='direct_flight'),
        path('allhosis/', views.Allroutes, name='allhospitals'),
        path('osip/', views.Osiptende, name='osiptende'),
        path('viable/', views.LocViable, name='viable' ),	

]

