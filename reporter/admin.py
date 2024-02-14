from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
# from import_export.admin import ImportExportModelAdmin
from . models import (
	Sample,
	Counties,
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
	



# # Register your models here.
class SampleAdmin(LeafletGeoAdmin):
	list_display = ('name', 'location')

class CountiesAdmin(LeafletGeoAdmin):
	list_display = ('county', 'county3_id')

class SubcountiesAdmin(LeafletGeoAdmin):
	list_display = ('name_3', 'name_1')

class SchoolsAdmin(LeafletGeoAdmin):
	list_display = ('name', 'level')

class AirportsAdmin(LeafletGeoAdmin):
	list_display = ('name','aeroway')

class PopulatedAdmin(LeafletGeoAdmin):
	list_display = ('name','population')

class WaterwaysdAdmin(LeafletGeoAdmin):
	list_display = ('name','source')

class HospitalsAdmin(LeafletGeoAdmin):
	list_display = ('facility_n','categoties')

class RoadsAdmin(LeafletGeoAdmin):
	list_display = ('name','highway')

class AgricAdmin(LeafletGeoAdmin):
	list_display = ('agid','agricultur')

class ProtectedareasAdmin(LeafletGeoAdmin):
	list_display = ('areaname','designate')

class WetlandsAdmin(LeafletGeoAdmin):
	list_display = ('userlabel','lccscode')




class HbAgricAdmin(LeafletGeoAdmin):
	list_display = ('agid','agricultur')

class HomabayAdmin(LeafletGeoAdmin):
	list_display = ('counties','codes')

class HBHealthFacAdmin(LeafletGeoAdmin):
	list_display = ('facility_n','categoties')

class HblakesAdmin(LeafletGeoAdmin):
	list_display = ('landcover','counties')

class HbprotectedAdmin(LeafletGeoAdmin):
	list_display = ('areaname','designate')

class HbRiversdAdmin(LeafletGeoAdmin):
	list_display = ('counties','length')

class HbRoadsdAdmin(LeafletGeoAdmin):
	list_display = ('kenroad_id','length')

class HbschdAdmin(LeafletGeoAdmin):
	list_display = ('name','level')

class HbSoilsAdmin(LeafletGeoAdmin):
	list_display = ('drai_descr','rdep_descr')

class HbsubAdmin(LeafletGeoAdmin):
	list_display = ('name_3','codes')



class HomaBayCsvAdmin(LeafletGeoAdmin):
    list_display = (
        'object_id', 'facility_n',"categories", 'owner', 'county', 'sub_county',
        'division', 'location','nearest_to',
        'latitude', 'longitude'
    )

class CompletehbhospAdmin(admin.ModelAdmin):
    list_display = ('object_id', 'facility_n', 'categories', 'owner', 'county', 'sub_county', 'division',
                    'location', 'sub_location', 'constituency', 'nearest_to', 'Code', 'Registration_number',
                    'Keph_level', 'Facility_type', 'Regulatory_body', 'Beds', 'Cots', 'Ward',
                    'Operation_status', 'Open_whole_day', 'Open_public_holidays', 'Open_weekends',
                    'Open_late_night', 'Approved', 'Public_visible', 'Closed', 'latitude', 'longitude')


class KephLevelAdmin(LeafletGeoAdmin):
	list_display=('id','level_1','level_2','level_3','level_4','level_5'
)


admin.site.register(Sample, SampleAdmin)
admin.site.register(Counties, CountiesAdmin)
admin.site.register(Sub_counties, SubcountiesAdmin)
admin.site.register(Schools, SchoolsAdmin)
admin.site.register(Airports,AirportsAdmin)
admin.site.register(Populated_Regions, PopulatedAdmin)
admin.site.register(WaterWays, WaterwaysdAdmin)
admin.site.register(Hospitals,HospitalsAdmin)
admin.site.register(Roads, RoadsAdmin)
admin.site.register(Agriculture, AgricAdmin)
admin.site.register(ProtectedAreas, ProtectedareasAdmin)
admin.site.register(WetLands,WetlandsAdmin)


admin.site.register(HbAgric, HbAgricAdmin)
admin.site.register(Homa_Bay, HomabayAdmin)
admin.site.register(H_B_HealthFacilities,HBHealthFacAdmin)
admin.site.register(Lakes, HblakesAdmin)
admin.site.register(HbProtectedAreas, HbprotectedAdmin)
admin.site.register(HbRivers, HbRiversdAdmin)
admin.site.register(HbRoads, HbRiversdAdmin)
admin.site.register(Hbschools, HbschdAdmin)
admin.site.register(Soils, HbSoilsAdmin)
admin.site.register(HbSubCounties,HbsubAdmin)


admin.site.register(HomaBayHospCsv, HomaBayCsvAdmin)
admin.site.register(CompltHospCsv, CompletehbhospAdmin)
admin.site.register(KephLevel, KephLevelAdmin)
