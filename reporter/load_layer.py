import os
from django.contrib.gis.utils import LayerMapping
from . models import (
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

    Hosis,
 
    )


# Auto-generated `LayerMapping` dictionary for Counties model
counties_mapping = {
    'objectid': 'OBJECTID',
    'area': 'AREA',
    'perimeter': 'PERIMETER',
    'county3_field': 'COUNTY3_',
    'county3_id': 'COUNTY3_ID',
    'county': 'COUNTY',
    'shape_leng': 'SHAPE_LENG',
    'shape_area': 'SHAPE_AREA',
    'x_coord': 'X_COORD',
    'y_coord': 'Y_COORD',
    'area_1': 'area_1',
    'geom': 'MULTIPOLYGON',
}

county_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),"E:/ilri_vector/county.shp"))

def run(verbose=True):
    lm = LayerMapping(Counties, county_shp, counties_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)



sub_counties_mapping = {
    'id_0': 'ID_0',
    'iso': 'ISO',
    'name_0': 'NAME_0',
    'id_1': 'ID_1',
    'name_1': 'NAME_1',
    'id_2': 'ID_2',
    'name_2': 'NAME_2',
    'id_3': 'ID_3',
    'name_3': 'NAME_3',
    'type_3': 'TYPE_3',
    'engtype_3': 'ENGTYPE_3',
    'nl_name_3': 'NL_NAME_3',
    'varname_3': 'VARNAME_3',
    'geom': 'MULTIPOLYGON',
}

subcounty_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),"E:/kenya/KEN_adm3.shp"))

def run(verbose=True):
    lm = LayerMapping(Sub_counties, subcounty_shp, sub_counties_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)


schools_mapping = {
    'name': 'Name',
    'province': 'PROVINCE',
    'district': 'DISTRICT',
    'costituenc': 'COSTITUENC',
    'division': 'DIVISION',
    'location': 'LOCATION',
    'sublocatio': 'SUBLOCATIO',
    'level': 'Level',
    'status': 'Status',
    'sponsor': 'Sponsor',
    'longitude': 'Longitude',
    'latitude': 'Latitude',
    'fclassro': 'FClassro',
    'geom': 'MULTIPOINT',
}
school_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),"E:/education_facilities_points/schools.shp"))

def run(verbose=True):
    lm = LayerMapping(Schools, school_shp, schools_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)



airports_mapping = {
    'osm_id': 'osm_id',
    'emergencyh': 'emergencyh',
    'building': 'building',
    'name': 'name',
    'source': 'source',
    'addrcity': 'addrcity',
    'emergency': 'emergency',
    'operatorty': 'operatorty',
    'addrfull': 'addrfull',
    'capacitype': 'capacitype',
    'aeroway': 'aeroway',
    'geom': 'MULTIPOINT',
}
airports_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),"C:/Users/opote/Downloads/hotosm_ken_airports_points_shp/hotosm_ken_airports_points.shp"))

def run(verbose=True):
    lm = LayerMapping(Airports, airports_shp, airports_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)


# Auto-generated `LayerMapping` dictionary for Populated_Regions model
populated_regions_mapping = {
    'osm_id': 'osm_id',
    'name': 'name',
    'source': 'source',
    'is_in': 'is_in',
    'place': 'place',
    'population': 'population',
    'geom': 'MULTIPOLYGON',
}
populated_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),"C:/Users/opote/Downloads/hotosm_ken_populated_places_polygons_shp/hotosm_ken_populated_places_polygons.shp"))

def run(verbose=True):
    lm = LayerMapping(Populated_Regions, populated_shp, populated_regions_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

waterways_mapping = {
    'osm_id': 'osm_id',
    'layer': 'layer',
    'name': 'name',
    'source': 'source',
    'covered': 'covered',
    'natural': 'natural',
    'waterway': 'waterway',
    'tunnel': 'tunnel',
    'water': 'water',
    'width': 'width',
    'depth': 'depth',
    'blockage': 'blockage',
    'geom': 'MULTIPOLYGON',
}
waterways_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),"C:/Users/opote/Downloads/hotosm_ken_waterways_polygons_shp/hotosm_ken_waterways_polygons.shp"))

def run(verbose=True):
    lm = LayerMapping(WaterWays, waterways_shp, waterways_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

hospitals_mapping = {
    'objectid': 'OBJECTID',
    'facility_n': 'Facility_N',
    'categoties': 'Categoties',
    'owner': 'Owner',
    'county': 'County',
    'sub_county': 'Sub_County',
    'division': 'Division',
    'location': 'Location',
    'sub_locati': 'Sub_Locati',
    'constituen': 'Constituen',
    'nearest_to': 'Nearest_To',
    'latitude': 'Latitude',
    'longitude': 'Longitude',
    'geom': 'MULTIPOINT',
}
hospitals_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),"C:/Users/opote/Desktop/kenya_health_facilities/Hospitals.shp"))

def run(verbose=True):
    lm = LayerMapping(Hospitals, hospitals_shp, hospitals_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

roads_mapping = {
    'osm_id': 'osm_id',
    'layer': 'layer',
    'name': 'name',
    'bridge': 'bridge',
    'smoothness': 'smoothness',
    'source': 'source',
    'width': 'width',
    'lanes': 'lanes',
    'oneway': 'oneway',
    'highway': 'highway',
    'surface': 'surface',
    'geom': 'MULTILINESTRING',
}
roads_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),"E:/my_data_backup/kenyan_roads/hotosm_ken_roads_lines_shp/hotosm_ken_roads_lines.shp"))

def run(verbose=True):
    lm = LayerMapping(Roads, roads_shp, roads_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)


agriculture_mapping = {
    'agid': 'AGID',
    'agricultur': 'AGRICULTUR',
    'geom': 'MULTIPOLYGON',
}
agriculture_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),"E:/ilri_vector/agriculture90.shp"))

def run(verbose=True):
    lm = LayerMapping(Agriculture, agriculture_shp, agriculture_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)




protectedareas_mapping = {
    'fid_new_am': 'FID_NEW_AM',
    'area': 'AREA',
    'perimeter': 'PERIMETER',
    'parknewdd_field': 'PARKNEWDD_',
    'parknewdd1': 'PARKNEWDD1',
    'name': 'NAME',
    'pta': 'PTA',
    'fid_nation': 'FID_NATION',
    'areaname': 'AREANAME',
    'iso3': 'ISO3',
    'lat': 'LAT',
    'lon': 'LON',
    'designate': 'DESIGNATE',
    'gisname': 'GISNAME',
    'source_id': 'SOURCE_ID',
    'iucncat': 'IUCNCAT',
    'status': 'STATUS',
    'shape_leng': 'SHAPE_LENG',
    'shape_area': 'SHAPE_AREA',
    'site_code': 'SITE_CODE',
    'country': 'COUNTRY',
    'marine': 'MARINE',
    'poly': 'POLY',
    'admin': 'ADMIN',
    'management': 'MANAGEMENT',
    'owner': 'OWNER',
    'est_date': 'EST_DATE',
    'area_ha': 'AREA_HA',
    'notes': 'NOTES',
    'source': 'SOURCE',
    'z000_visit': 'Z000_VISIT',
    'vistor_ha': 'VISTOR_HA',
    'perc_visit': 'PERC_VISIT',
    'area_sqkm_field': 'AREA_SQKM_',
    'fid_nati_1': 'FID_NATI_1',
    'areaname_1': 'AREANAME_1',
    'iso3_1': 'ISO3_1',
    'lat_1': 'LAT_1',
    'lon_1': 'LON_1',
    'designat_1': 'DESIGNAT_1',
    'gisname_1': 'GISNAME_1',
    'source_i_1': 'SOURCE_I_1',
    'iucncat_1': 'IUCNCAT_1',
    'status_1': 'STATUS_1',
    'shape_le_1': 'SHAPE_LE_1',
    'shape_ar_1': 'SHAPE_AR_1',
    'site_cod_1': 'SITE_COD_1',
    'country_1': 'COUNTRY_1',
    'marine_1': 'MARINE_1',
    'poly_1': 'POLY_1',
    'admin_1': 'ADMIN_1',
    'manageme_1': 'MANAGEME_1',
    'owner_1': 'OWNER_1',
    'est_date_1': 'EST_DATE_1',
    'area_ha_1': 'AREA_HA_1',
    'notes_1': 'NOTES_1',
    'source_1': 'SOURCE_1',
    'z000_vis_1': 'Z000_VIS_1',
    'vistor_h_1': 'VISTOR_H_1',
    'perc_vis_1': 'PERC_VIS_1',
    'area_sqkm1': 'AREA_SQKM1',
    'geom': 'MULTIPOLYGON',
}

protectedareas_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),"E:/ilri_vector/protected_areas.shp"))

def run(verbose=True):
    lm = LayerMapping(ProtectedAreas, protectedareas_shp, protectedareas_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

wetlands_mapping = {
    'userlabel': 'USERLABEL',
    'lccscode': 'LCCSCODE',
    'area_sqkm_field': 'AREA_SQKM_',
    'wetland': 'WETLAND',
    'geom': 'MULTIPOLYGON',
}
wetlands_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),"E:/ilri_vector/wetlands.shp"))

def run(verbose=True):
    lm = LayerMapping(WetLands, wetlands_shp, wetlands_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)




# Homa-Bay Data
hbagric_mapping = {
    'agid': 'AGID',
    'agricultur': 'AGRICULTUR',
    'counties': 'Counties',
    'codes': 'Codes',
    'cty_code': 'Cty_CODE',
    'dis': 'dis',
    'geom': 'MULTIPOLYGON',
}
hbagric_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),"C:/Users/opote/Desktop/Homabay_data/AgricAreas.shp"))

def run(verbose=True):
    lm = LayerMapping(HbAgric, hbagric_shp, hbagric_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)


homa_bay_mapping = {
    'counties': 'Counties',
    'codes': 'Codes',
    'cty_code': 'Cty_CODE',
    'dis': 'dis',
    'geom': 'MULTIPOLYGON',
}
homa_bay_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),"C:/Users/opote/Desktop/Homabay_data/County.shp"))

def run(verbose=True):
    lm = LayerMapping(Homa_Bay, homa_bay_shp, homa_bay_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

h_b_healthfacilities_mapping = {
    'objectid': 'OBJECTID',
    'facility_n': 'Facility_N',
    'categoties': 'Categoties',
    'owner': 'Owner',
    'county': 'County',
    'sub_county': 'Sub_County',
    'division': 'Division',
    'location': 'Location',
    'sub_locati': 'Sub_Locati',
    'constituen': 'Constituen',
    'nearest_to': 'Nearest_To',
    'latitude': 'Latitude',
    'longitude': 'Longitude',
    'counties': 'Counties',
    'codes': 'Codes',
    'cty_code': 'Cty_CODE',
    'dis': 'dis',
    'geom': 'MULTIPOINT',
}
h_b_healthfacilities_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),"C:/Users/opote/Desktop/Homabay_data/HealthFacilities.shp"))

def run(verbose=True):
    lm = LayerMapping(H_B_HealthFacilities, h_b_healthfacilities_shp, h_b_healthfacilities_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

lakes_mapping = {
    'lcid': 'LCID',
    'landcover': 'LANDCOVER',
    'counties': 'Counties',
    'codes': 'Codes',
    'cty_code': 'Cty_CODE',
    'dis': 'dis',
    'geom': 'MULTIPOLYGON',
}
lakes_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),"C:/Users/opote/Desktop/Homabay_data/lakes.shp"))

def run(verbose=True):
    lm = LayerMapping(Lakes, lakes_shp, lakes_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)



protectedareas_mapping = {
    'fid_new_am': 'FID_NEW_AM',
    'area': 'AREA',
    'perimeter': 'PERIMETER',
    'parknewdd_field': 'PARKNEWDD_',
    'parknewdd1': 'PARKNEWDD1',
    'name': 'NAME',
    'pta': 'PTA',
    'fid_nation': 'FID_NATION',
    'areaname': 'AREANAME',
    'iso3': 'ISO3',
    'lat': 'LAT',
    'lon': 'LON',
    'designate': 'DESIGNATE',
    'gisname': 'GISNAME',
    'source_id': 'SOURCE_ID',
    'iucncat': 'IUCNCAT',
    'status': 'STATUS',
    'shape_leng': 'SHAPE_LENG',
    'shape_area': 'SHAPE_AREA',
    'site_code': 'SITE_CODE',
    'country': 'COUNTRY',
    'marine': 'MARINE',
    'poly': 'POLY',
    'admin': 'ADMIN',
    'management': 'MANAGEMENT',
    'owner': 'OWNER',
    'est_date': 'EST_DATE',
    'area_ha': 'AREA_HA',
    'notes': 'NOTES',
    'source': 'SOURCE',
    'z000_visit': 'Z000_VISIT',
    'vistor_ha': 'VISTOR_HA',
    'perc_visit': 'PERC_VISIT',
    'area_sqkm_field': 'AREA_SQKM_',
    'fid_nati_1': 'FID_NATI_1',
    'areaname_1': 'AREANAME_1',
    'iso3_1': 'ISO3_1',
    'lat_1': 'LAT_1',
    'lon_1': 'LON_1',
    'designat_1': 'DESIGNAT_1',
    'gisname_1': 'GISNAME_1',
    'source_i_1': 'SOURCE_I_1',
    'iucncat_1': 'IUCNCAT_1',
    'status_1': 'STATUS_1',
    'shape_le_1': 'SHAPE_LE_1',
    'shape_ar_1': 'SHAPE_AR_1',
    'site_cod_1': 'SITE_COD_1',
    'country_1': 'COUNTRY_1',
    'marine_1': 'MARINE_1',
    'poly_1': 'POLY_1',
    'admin_1': 'ADMIN_1',
    'manageme_1': 'MANAGEME_1',
    'owner_1': 'OWNER_1',
    'est_date_1': 'EST_DATE_1',
    'area_ha_1': 'AREA_HA_1',
    'notes_1': 'NOTES_1',
    'source_1': 'SOURCE_1',
    'z000_vis_1': 'Z000_VIS_1',
    'vistor_h_1': 'VISTOR_H_1',
    'perc_vis_1': 'PERC_VIS_1',
    'area_sqkm1': 'AREA_SQKM1',
    'counties': 'Counties',
    'codes': 'Codes',
    'cty_code': 'Cty_CODE',
    'dis': 'dis',
    'geom': 'MULTIPOLYGON',
}
protectedareas_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),"C:/Users/opote/Desktop/Homabay_data/ProtectedAreas.shp"))

def run(verbose=True):
    lm = LayerMapping(HbProtectedAreas, protectedareas_shp, protectedareas_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

hbrivers_mapping = {
    'fnode_field': 'FNODE_',
    'tnode_field': 'TNODE_',
    'lpoly_field': 'LPOLY_',
    'rpoly_field': 'RPOLY_',
    'length': 'LENGTH',
    'klrivers_field': 'KLRIVERS_',
    'klrivers_i': 'KLRIVERS_I',
    'length_1': 'length_1',
    'counties': 'Counties',
    'codes': 'Codes',
    'cty_code': 'Cty_CODE',
    'dis': 'dis',
    'geom': 'MULTILINESTRING',
}
hbrivers_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),"C:/Users/opote/Desktop/Homabay_data/Rivers.shp"))

def run(verbose=True):
    lm = LayerMapping(HbRivers, hbrivers_shp, hbrivers_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)


hbroads_mapping = {
    'fnode_field': 'FNODE_',
    'tnode_field': 'TNODE_',
    'lpoly_field': 'LPOLY_',
    'rpoly_field': 'RPOLY_',
    'length': 'LENGTH',
    'kenroad_field': 'KENROAD_',
    'kenroad_id': 'KENROAD_ID',
    'counties': 'Counties',
    'codes': 'Codes',
    'cty_code': 'Cty_CODE',
    'dis': 'dis',
    'geom': 'MULTILINESTRING',
}
hbroads_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),"C:/Users/opote/Desktop/Homabay_data/roads.shp"))

def run(verbose=True):
    lm = LayerMapping(HbRoads, hbroads_shp, hbroads_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)


hbschools_mapping = {
    'name': 'Name',
    'province': 'PROVINCE',
    'district': 'DISTRICT',
    'costituenc': 'COSTITUENC',
    'division': 'DIVISION',
    'location': 'LOCATION',
    'sublocatio': 'SUBLOCATIO',
    'level': 'Level',
    'status': 'Status',
    'sponsor': 'Sponsor',
    'longitude': 'Longitude',
    'latitude': 'Latitude',
    'f_classro': 'F__Classro',
    'counties': 'Counties',
    'codes': 'Codes',
    'cty_code': 'Cty_CODE',
    'dis': 'dis',
    'geom': 'MULTIPOINT',
}
hbschools_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),"C:/Users/opote/Desktop/Homabay_data/schools.shp"))

def run(verbose=True):
    lm = LayerMapping(Hbschools, hbschools_shp, hbschools_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)

soils_mapping = {
    'area': 'AREA',
    'perimeter': 'PERIMETER',
    'ilrifnl_field': 'ILRIFNL_',
    'suid': 'SUID',
    'bedr': 'BEDR',
    'sdra': 'SDRA',
    'sdra_descr': 'SDRA_DESCR',
    'prop': 'PROP',
    'prid': 'PRID',
    'phaq': 'PHAQ',
    'phkc': 'PHKC',
    'exna': 'EXNA',
    'exck': 'EXCK',
    'cecs': 'CECS',
    'drai': 'DRAI',
    'drai_descr': 'DRAI_DESCR',
    'rdep': 'RDEP',
    'rdep_descr': 'RDEP_DESCR',
    'lith': 'LITH',
    'slop': 'SLOP',
    'reli': 'RELI',
    'soil': 'SOIL',
    'sid': 'SID',
    'clay': 'CLAY',
    'clay_descr': 'CLAY_DESCR',
    'text': 'TEXT',
    'text_descr': 'TEXT_DESCR',
    'rslo': 'RSLO',
    'rslo_descr': 'RSLO_DESCR',
    'lndf': 'LNDF',
    'lndf_descr': 'LNDF_DESCR',
    'counties': 'Counties',
    'codes': 'Codes',
    'cty_code': 'Cty_CODE',
    'dis': 'dis',
    'geom': 'MULTIPOLYGON',
}
soils_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),"C:/Users/opote/Desktop/Homabay_data/Soils.shp"))

def run(verbose=True):
    lm = LayerMapping(Soils, soils_shp, soils_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)



hbsubcounties_mapping = {
    'id_0': 'ID_0',
    'iso': 'ISO',
    'name_0': 'NAME_0',
    'id_1': 'ID_1',
    'name_1': 'NAME_1',
    'id_2': 'ID_2',
    'name_2': 'NAME_2',
    'id_3': 'ID_3',
    'name_3': 'NAME_3',
    'type_3': 'TYPE_3',
    'engtype_3': 'ENGTYPE_3',
    'nl_name_3': 'NL_NAME_3',
    'varname_3': 'VARNAME_3',
    'counties': 'Counties',
    'codes': 'Codes',
    'cty_code': 'Cty_CODE',
    'dis': 'dis',
    'geom': 'MULTIPOLYGON',
}
hbsubcounties_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),"C:/Users/opote/Desktop/Homabay_data/sub_counties.shp"))

def run(verbose=True):
    lm = LayerMapping(HbSubCounties, hbsubcounties_shp, hbsubcounties_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)


# hosis_mapping = {
#     'object_id': 'object_id',
#     'facility_n': 'facility_n',
#     'categories': 'categories',
#     'owner': 'owner',
#     'county': 'county',
#     'sub_county': 'sub_county',
#     'division': 'division',
#     'location': 'location',
#     'sub_locati': 'sub_locati',
#     'constituen': 'constituen',
#     'nearest_to': 'nearest_to',
#     'code': 'Code',
#     'registrati': 'Registrati',
#     'keph_level': 'Keph_level',
#     'facility_t': 'Facility_t',
#     'owners': 'Owners',
#     'regulatory': 'Regulatory',
#     'beds': 'Beds',
#     'cots': 'Cots',
#     'ward': 'Ward',
#     'operation': 'Operation',
#     'open_whole': 'Open_whole',
#     'open_publi': 'Open_publi',
#     'open_weeke': 'Open_weeke',
#     'open_late_field': 'Open_late_',
#     'approved': 'Approved',
#     'public_vis': 'Public_vis',
#     'closed': 'Closed',
#     'latitude': 'latitude',
#     'longitude': 'longitude',
#     'geom': 'MULTILINESTRING',
# }
# hosis_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),"C:/Users/opote/Desktop/Homabay_data/(HB)health_facilities.shp"))

# def run(verbose=True):
#     lm = LayerMapping(Hosis, hosis_shp, hosis_mapping, transform=False, encoding='iso-8859-1')
#     lm.save(strict=True, verbose=verbose)

