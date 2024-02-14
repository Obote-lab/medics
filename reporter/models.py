from django.db import models
from django.contrib.gis.db import models


# Create your models here.

class Sample(models.Model):
	name           = models.CharField(max_length=200,unique=True)
	location       = models.PointField(srid=4326)
	objects        = models.Manager()


	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Samples'



class Counties(models.Model):
    objectid            = models.IntegerField(null=True)
    area                = models.FloatField(null=True)
    perimeter           = models.FloatField(null=True)
    county3_field       = models.FloatField(null=True)
    county3_id          = models.FloatField(null=True)
    county              = models.CharField(max_length=20, null=True)
    shape_leng          = models.FloatField(null=True)
    shape_area          = models.FloatField(null=True)
    x_coord             = models.FloatField(null=True)
    y_coord             = models.FloatField(null=True)
    area_1              = models.BigIntegerField(null=True)
    geom                = models.MultiPolygonField(srid=4326)

    def __str__(self): 
        return self.county
class Sub_counties(models.Model):
    id_0            = models.BigIntegerField(null=True)
    iso             = models.CharField(max_length=3, null=True)
    name_0          = models.CharField(max_length=75, null=True)
    id_1            = models.BigIntegerField(null=True)
    name_1          = models.CharField(max_length=75, null=True)
    id_2            = models.BigIntegerField(null=True)
    name_2          = models.CharField(max_length=75, null=True)
    id_3            = models.BigIntegerField(null=True)
    name_3          = models.CharField(max_length=75, null=True)
    type_3          = models.CharField(max_length=50, null=True)
    engtype_3       = models.CharField(max_length=50, null=True)
    nl_name_3       = models.CharField(max_length=75, null=True)
    varname_3       = models.CharField(max_length=100, null=True)
    geom            = models.MultiPolygonField(srid=4326)

    def __str__(self): 
        return self.name_3


class Schools(models.Model):
    name            = models.CharField(max_length=80, null=True)
    province        = models.CharField(max_length=80, null=True)
    district        = models.CharField(max_length=80, null=True)
    costituenc      = models.CharField(max_length=80, null=True)
    division        = models.CharField(max_length=80, null=True)
    location        = models.CharField(max_length=80, null=True)
    sublocatio      = models.CharField(max_length=80, null=True)
    level           = models.CharField(max_length=80, null=True)
    status          = models.CharField(max_length=80, null=True)
    sponsor         = models.CharField(max_length=80, null=True)
    longitude       = models.FloatField(null=True)
    latitude        = models.FloatField(null=True)
    fclassro        = models.BigIntegerField(null=True)
    geom            = models.MultiPointField(srid=4326)

    def __str__(self): 
        return self.name


class Airports(models.Model):
    osm_id          = models.FloatField(null=True)
    emergencyh      = models.CharField(max_length=80, null=True)
    building        = models.CharField(max_length=80, null=True)
    name            = models.CharField(max_length=80, null=True)
    source          = models.CharField(max_length=80, null=True)
    addrcity        = models.CharField(max_length=80, null=True)
    emergency       = models.CharField(max_length=80, null=True)
    operatorty      = models.CharField(max_length=80, null=True)
    addrfull        = models.CharField(max_length=80, null=True)
    capacitype      = models.CharField(max_length=80, null=True)
    aeroway         = models.CharField(max_length=80, null=True)
    geom            = models.MultiPointField(srid=4326)



    def __str__(self):
        if self.name is not None:
            return str(self.name)
        else:
            return "Name Not Provided"  

class Populated_Regions(models.Model):
    osm_id          = models.FloatField(null=True)
    name            = models.CharField(max_length=80, null=True)
    source          = models.CharField(max_length=80, null=True)
    is_in           = models.CharField(max_length=80, null=True)
    place           = models.CharField(max_length=80, null=True)
    population      = models.CharField(max_length=80, null=True)
    geom            = models.MultiPolygonField(srid=4326)

    def __str__(self):
        if self.name is not None:
            return str(self.name)
        else:
            return "Name Not Provided"  



class WaterWays(models.Model):
    osm_id          = models.FloatField(null=True)
    layer           = models.CharField(max_length=80, null=True)
    name            = models.CharField(max_length=80, null=True)
    source          = models.CharField(max_length=80, null=True)
    covered         = models.CharField(max_length=80, null=True)
    natural         = models.CharField(max_length=80, null=True)
    waterway        = models.CharField(max_length=80, null=True)
    tunnel          = models.CharField(max_length=80, null=True)
    water           = models.CharField(max_length=80, null=True)
    width           = models.CharField(max_length=80, null=True)
    depth           = models.CharField(max_length=80, null=True)
    blockage        = models.CharField(max_length=80, null=True)
    geom            = models.MultiPolygonField(srid=4326)

    def __str__(self):
        if self.name is not None:
            return str(self.name)
        else:
            return "Name Not Provided" 

class Hospitals(models.Model):
    objectid        = models.BigIntegerField(null=True)
    facility_n      = models.CharField(max_length=80, null=True)
    categoties      = models.CharField(max_length=80, null=True)
    owner           = models.CharField(max_length=80, null=True)
    county          = models.CharField(max_length=80, null=True)
    sub_county      = models.CharField(max_length=80, null=True)
    division        = models.CharField(max_length=80, null=True)
    location        = models.CharField(max_length=80, null=True)
    sub_locati      = models.CharField(max_length=80, null=True)
    constituen      = models.CharField(max_length=80, null=True)
    nearest_to      = models.CharField(max_length=85, null=True)
    latitude        = models.FloatField(null=True)
    longitude       = models.FloatField(null=True)
    geom            = models.MultiPointField(srid=4326)

    def __str__(self): 
        return self.facility_n

class Roads(models.Model):
    osm_id          = models.FloatField(null=True)
    layer           = models.CharField(max_length=80, null=True)
    name            = models.CharField(max_length=80, null=True)
    bridge          = models.CharField(max_length=80, null=True)
    smoothness      = models.CharField(max_length=80, null=True)
    source          = models.CharField(max_length=81, null=True)
    width           = models.CharField(max_length=80, null=True)
    lanes           = models.CharField(max_length=80, null=True)
    oneway          = models.CharField(max_length=80, null=True)
    highway         = models.CharField(max_length=80, null=True)
    surface         = models.CharField(max_length=80, null=True)
    geom            = models.MultiLineStringField(srid=4326)

    def __str__(self):
        if self.name is not None:
            return str(self.name)
        else:
            return "Name Not Provided" 

class Agriculture(models.Model):
    agid                = models.CharField(max_length=15, null=True)
    agricultur          = models.CharField(max_length=254, null=True)
    geom                = models.MultiPolygonField(srid=4326)

    def __str__(self): 
        return self.agricultur

class ProtectedAreas(models.Model):
    fid_new_am              = models.IntegerField(null=True)
    area                    = models.FloatField(null=True)
    perimeter               = models.FloatField(null=True)
    parknewdd_field         = models.BigIntegerField(null=True)
    parknewdd1              = models.BigIntegerField(null=True)
    name                    = models.CharField(max_length=20, null=True)
    pta                     = models.IntegerField(null=True)
    fid_nation              = models.IntegerField(null=True)
    areaname                = models.CharField(max_length=120, null=True)
    iso3                    = models.CharField(max_length=3, null=True)
    lat                     = models.FloatField(null=True)
    lon                     = models.FloatField(null=True)
    designate               = models.CharField(max_length=100, null=True)
    gisname                 = models.CharField(max_length=80, null=True)
    source_id               = models.CharField(max_length=6, null=True)
    iucncat                 = models.CharField(max_length=8, null=True)
    status                  = models.CharField(max_length=30, null=True)
    shape_leng              = models.FloatField(null=True)
    shape_area              = models.FloatField(null=True)
    site_code               = models.IntegerField(null=True)
    country                 = models.CharField(max_length=50, null=True)
    marine                  = models.CharField(max_length=254, null=True)
    poly                    = models.CharField(max_length=254, null=True)
    admin                   = models.CharField(max_length=200, null=True)
    management              = models.CharField(max_length=200, null=True)
    owner                   = models.CharField(max_length=50, null=True)
    est_date                = models.DateField(null=True)
    area_ha                 = models.FloatField(null=True)
    notes                   = models.CharField(max_length=254, null=True)
    source                  = models.CharField(max_length=254, null=True)
    z000_visit              = models.FloatField(null=True)
    vistor_ha               = models.FloatField(null=True)
    perc_visit              = models.FloatField(null=True)
    area_sqkm_field         = models.FloatField(null=True)
    fid_nati_1              = models.IntegerField(null=True)
    areaname_1              = models.CharField(max_length=120, null=True)
    iso3_1                  = models.CharField(max_length=3, null=True)
    lat_1                   = models.FloatField(null=True)
    lon_1                   = models.FloatField(null=True)
    designat_1              = models.CharField(max_length=100, null=True)
    gisname_1               = models.CharField(max_length=80, null=True)
    source_i_1              = models.CharField(max_length=6, null=True)
    iucncat_1               = models.CharField(max_length=8, null=True)
    status_1                = models.CharField(max_length=30, null=True)
    shape_le_1              = models.FloatField(null=True)
    shape_ar_1              = models.FloatField(null=True)
    site_cod_1              = models.IntegerField(null=True)
    country_1               = models.CharField(max_length=50, null=True)
    marine_1                = models.CharField(max_length=254, null=True)
    poly_1                  = models.CharField(max_length=254, null=True)
    admin_1                 = models.CharField(max_length=200, null=True)
    manageme_1              = models.CharField(max_length=200, null=True)
    owner_1                 = models.CharField(max_length=50, null=True)
    est_date_1              = models.DateField(null=True)
    area_ha_1               = models.FloatField(null=True)
    notes_1                 = models.CharField(max_length=254, null=True)
    source_1                = models.CharField(max_length=254, null=True)
    z000_vis_1              = models.FloatField(null=True)
    vistor_h_1              = models.FloatField(null=True)
    perc_vis_1              = models.FloatField(null=True)
    area_sqkm1              = models.FloatField(null=True)
    geom                    = models.MultiPolygonField(srid=4326)

    def __str__(self):
        if self.areaname is not None:
            return str(self.areaname)
        else:
            return "Name Not Provided" 

class WetLands(models.Model):
    userlabel           = models.CharField(max_length=40, null=True)
    lccscode            = models.CharField(max_length=250, null=True)
    area_sqkm_field     = models.FloatField(null=True)
    wetland             = models.IntegerField(null=True)
    geom                = models.MultiPolygonField(srid=4326)

    def __str__(self): 
        return self.userlabel








        # hb dataset models


class HbAgric(models.Model):
    agid            = models.CharField(max_length=80, null=True)
    agricultur      = models.CharField(max_length=105, null=True)
    counties        = models.CharField(max_length=80, null=True)
    codes           = models.BigIntegerField(null=True)
    cty_code        = models.CharField(max_length=80, null=True)
    dis             = models.BigIntegerField(null=True)
    geom            = models.MultiPolygonField(srid=4326)

    def __str__(self): 
        return self.agricultur

class Homa_Bay(models.Model):
    counties        = models.CharField(max_length=25, null=True)
    codes           = models.IntegerField(null=True)
    cty_code        = models.CharField(max_length=24, null=True)
    dis             = models.IntegerField(null=True)
    geom            = models.MultiPolygonField(srid=4326)

    def __str__(self): 
        return self.counties

class H_B_HealthFacilities(models.Model):
    objectid            = models.BigIntegerField(null=True)
    facility_n          = models.CharField(max_length=80, null=True)
    categoties          = models.CharField(max_length=80, null=True)
    owner               = models.CharField(max_length=80, null=True)
    county              = models.CharField(max_length=80, null=True)
    sub_county          = models.CharField(max_length=80, null=True)
    division            = models.CharField(max_length=80, null=True)
    location            = models.CharField(max_length=80, null=True)
    sub_locati          = models.CharField(max_length=80, null=True)
    constituen          = models.CharField(max_length=80, null=True)
    nearest_to          = models.CharField(max_length=80, null=True)
    latitude            = models.FloatField(null=True)
    longitude           = models.FloatField(null=True)
    counties            = models.CharField(max_length=80, null=True)
    codes               = models.BigIntegerField(null=True)
    cty_code            = models.CharField(max_length=80, null=True)
    dis                 = models.BigIntegerField(null=True)
    geom                = models.MultiPointField(srid=4326)

    def __str__(self): 
        return self.facility_n

class Lakes(models.Model):
    lcid            = models.CharField(max_length=80, null=True)
    landcover       = models.CharField(max_length=80, null=True)
    counties        = models.CharField(max_length=80, null=True)
    codes           = models.BigIntegerField(null=True)
    cty_code        = models.CharField(max_length=80, null=True)
    dis             = models.BigIntegerField(null=True)
    geom            = models.MultiPolygonField(srid=4326)

    def __str__(self): 
        return self.landcover


class HbProtectedAreas(models.Model):
    fid_new_am          = models.BigIntegerField(null=True)
    area                = models.FloatField(null=True)
    perimeter           = models.FloatField(null=True)
    parknewdd_field     = models.BigIntegerField(null=True)
    parknewdd1          = models.BigIntegerField(null=True)
    name                = models.CharField(max_length=80, null=True)
    pta                 = models.BigIntegerField(null=True)
    fid_nation          = models.BigIntegerField(null=True)
    areaname            = models.CharField(max_length=80, null=True)
    iso3                = models.CharField(max_length=80, null=True)
    lat                 = models.FloatField(null=True)
    lon                 = models.FloatField(null=True)
    designate           = models.CharField(max_length=80, null=True)
    gisname             = models.CharField(max_length=80, null=True)
    source_id           = models.CharField(max_length=80, null=True)
    iucncat             = models.CharField(max_length=80, null=True)
    status              = models.CharField(max_length=80, null=True)
    shape_leng          = models.FloatField(null=True)
    shape_area          = models.FloatField(null=True)
    site_code           = models.BigIntegerField(null=True)
    country             = models.CharField(max_length=80, null=True)
    marine              = models.CharField(max_length=80, null=True)
    poly                = models.CharField(max_length=80, null=True)
    admin               = models.CharField(max_length=80, null=True)
    management          = models.CharField(max_length=80, null=True)
    owner               = models.CharField(max_length=80, null=True)
    est_date            = models.CharField(max_length=80, null=True)
    area_ha             = models.FloatField(null=True)
    notes               = models.FloatField(null=True)
    source              = models.CharField(max_length=80, null=True)
    z000_visit          = models.FloatField(null=True)
    vistor_ha           = models.FloatField(null=True)
    perc_visit          = models.FloatField(null=True)
    area_sqkm_field     = models.FloatField(null=True)
    fid_nati_1          = models.BigIntegerField(null=True)
    areaname_1          = models.CharField(max_length=80, null=True)
    iso3_1              = models.CharField(max_length=80, null=True)
    lat_1               = models.FloatField(null=True)
    lon_1               = models.FloatField(null=True)
    designat_1          = models.CharField(max_length=80, null=True)
    gisname_1           = models.CharField(max_length=80, null=True)
    source_i_1          = models.CharField(max_length=80, null=True)
    iucncat_1           = models.CharField(max_length=80, null=True)
    status_1            = models.CharField(max_length=80, null=True)
    shape_le_1          = models.FloatField(null=True)
    shape_ar_1          = models.FloatField(null=True)
    site_cod_1          = models.BigIntegerField(null=True)
    country_1           = models.CharField(max_length=80, null=True)
    marine_1            = models.CharField(max_length=80, null=True)
    poly_1              = models.CharField(max_length=80, null=True)
    admin_1             = models.CharField(max_length=80, null=True)
    manageme_1          = models.CharField(max_length=80, null=True)
    owner_1             = models.CharField(max_length=80, null=True)
    est_date_1          = models.CharField(max_length=80, null=True)
    area_ha_1           = models.FloatField(null=True)
    notes_1             = models.FloatField(null=True)
    source_1            = models.CharField(max_length=80, null=True)
    z000_vis_1          = models.FloatField(null=True)
    vistor_h_1          = models.FloatField(null=True)
    perc_vis_1          = models.FloatField(null=True)
    area_sqkm1          = models.FloatField(null=True)
    counties            = models.CharField(max_length=80, null=True)
    codes               = models.BigIntegerField(null=True)
    cty_code            = models.CharField(max_length=80, null=True)
    dis                 = models.BigIntegerField(null=True)
    geom                = models.MultiPolygonField(srid=4326)

    def __str__(self): 
        return self.areaname

class HbRivers(models.Model):
    fnode_field         = models.BigIntegerField(null=True)
    tnode_field         = models.BigIntegerField(null=True)
    lpoly_field         = models.BigIntegerField(null=True)
    rpoly_field         = models.BigIntegerField(null=True)
    length              = models.FloatField(null=True)
    klrivers_field      = models.BigIntegerField(null=True)
    klrivers_i          = models.BigIntegerField(null=True)
    length_1            = models.BigIntegerField(null=True)
    counties            = models.CharField(max_length=80, null=True)
    codes               = models.BigIntegerField(null=True)
    cty_code            = models.CharField(max_length=80, null=True)
    dis                 = models.BigIntegerField(null=True)
    geom                = models.MultiLineStringField(srid=4326)

    def __str__(self): 
        return self.cty_code

class HbRoads(models.Model):
    fnode_field          = models.BigIntegerField(null=True)
    tnode_field          = models.BigIntegerField(null=True)
    lpoly_field          = models.BigIntegerField(null=True)
    rpoly_field          = models.BigIntegerField(null=True)
    length               = models.FloatField(null=True)
    kenroad_field        = models.BigIntegerField(null=True)
    kenroad_id           = models.BigIntegerField(null=True)
    counties             = models.CharField(max_length=80, null=True)
    codes                = models.BigIntegerField(null=True)
    cty_code             = models.CharField(max_length=80, null=True)
    dis                  = models.BigIntegerField(null=True)
    geom                 = models.MultiLineStringField(srid=4326)

    def __str__(self):
        if self.kenroad_id is not None:
            return str(self.kenroad_id)
        else:
            return "kenroad_id Not Provided" 

class Hbschools(models.Model):
    name            = models.CharField(max_length=80, null=True)
    province        = models.CharField(max_length=80, null=True)
    district        = models.CharField(max_length=80, null=True)
    costituenc      = models.CharField(max_length=80, null=True)
    division        = models.CharField(max_length=80, null=True)
    location        = models.CharField(max_length=80, null=True)
    sublocatio      = models.CharField(max_length=80, null=True)
    level           = models.CharField(max_length=80, null=True)
    status          = models.CharField(max_length=80, null=True)
    sponsor         = models.CharField(max_length=80, null=True)
    longitude       = models.FloatField(null=True)
    latitude        = models.FloatField(null=True)
    f_classro       = models.BigIntegerField(null=True)
    counties        = models.CharField(max_length=80, null=True)
    codes           = models.BigIntegerField(null=True)
    cty_code        = models.CharField(max_length=80, null=True)
    dis             = models.BigIntegerField(null=True)
    geom            = models.MultiPointField(srid=4326)

    def __str__(self): 
        return self.name

class Soils(models.Model):
    area            = models.FloatField(null=True)
    perimeter       = models.FloatField(null=True)
    ilrifnl_field   = models.BigIntegerField(null=True)
    suid            = models.BigIntegerField(null=True)
    bedr            = models.FloatField(null=True)
    sdra            = models.CharField(max_length=80, null=True)
    sdra_descr      = models.CharField(max_length=80, null=True)
    prop            = models.BigIntegerField(null=True)
    prid            = models.CharField(max_length=80, null=True)
    phaq            = models.FloatField(null=True)
    phkc            = models.FloatField(null=True)
    exna            = models.FloatField(null=True)
    exck            = models.FloatField(null=True)
    cecs            = models.FloatField(null=True)
    drai            = models.CharField(max_length=80, null=True)
    drai_descr      = models.CharField(max_length=80, null=True)
    rdep            = models.CharField(max_length=80, null=True)
    rdep_descr      = models.CharField(max_length=80, null=True)
    lith            = models.CharField(max_length=80, null=True)
    slop            = models.BigIntegerField(null=True)
    reli            = models.BigIntegerField(null=True)
    soil            = models.CharField(max_length=80, null=True)
    sid             = models.BigIntegerField(null=True)
    clay            = models.CharField(max_length=80, null=True)
    clay_descr      = models.CharField(max_length=80, null=True)
    text            = models.CharField(max_length=80, null=True)
    text_descr      = models.CharField(max_length=80, null=True)
    rslo            = models.CharField(max_length=80, null=True)
    rslo_descr      = models.CharField(max_length=80, null=True)
    lndf            = models.CharField(max_length=80, null=True)
    lndf_descr      = models.CharField(max_length=80, null=True)
    counties        = models.CharField(max_length=80, null=True)
    codes           = models.BigIntegerField(null=True)
    cty_code        = models.CharField(max_length=80, null=True)
    dis             = models.BigIntegerField(null=True)
    geom            = models.MultiPolygonField(srid=4326)

    def __str__(self):
        if self.drai_descr is not None:
            return str(self.drai_descr)
        else:
            return "Drainage description Not Provided" 

class HbSubCounties(models.Model):
    id_0            = models.BigIntegerField(null=True)
    iso             = models.CharField(max_length=80, null=True)
    name_0          = models.CharField(max_length=80, null=True)
    id_1            = models.BigIntegerField(null=True)
    name_1          = models.CharField(max_length=80, null=True)
    id_2            = models.BigIntegerField(null=True)
    name_2          = models.CharField(max_length=80, null=True)
    id_3            = models.BigIntegerField(null=True)
    name_3          = models.CharField(max_length=80, null=True)
    type_3          = models.CharField(max_length=80, null=True)
    engtype_3       = models.CharField(max_length=80, null=True)
    nl_name_3       = models.FloatField(null=True)
    varname_3       = models.FloatField(null=True)
    counties        = models.CharField(max_length=255)
    codes           = models.BigIntegerField(null=True)
    cty_code        = models.CharField(max_length=80, null=True)
    dis             = models.BigIntegerField(null=True)
    geom            = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.name_3


class HomaBayHospCsv(models.Model):
    object_id       = models.IntegerField(primary_key=True)
    facility_n      = models.CharField(max_length=255)
    categories      = models.CharField(max_length=255)
    owner           = models.CharField(max_length=80, null=True)
    county          = models.CharField(max_length=80, null=True)
    sub_county      = models.CharField(max_length=80, null=True)
    division        = models.CharField(max_length=80, null=True)
    location        = models.CharField(max_length=80, null=True)
    sub_location    = models.CharField(max_length=80, null=True)
    constituency    = models.CharField(max_length=80, null=True)
    nearest_to      = models.CharField(max_length=80, null=True)
    latitude        = models.DecimalField(max_digits=30, decimal_places=12,default=0)
    longitude       = models.DecimalField(max_digits=30, decimal_places=12,default=0)
    def __str__(self): 
        return self.facility_n
    class Meta:
        verbose_name_plural = 'HomaBayHospCsv'

# KEPH LEVEL 
class KephLevel(models.Model):
    id          = models.IntegerField(primary_key=True)
    level_1     = models.CharField(max_length=1000000)
    level_2     = models.CharField(max_length=1000000)
    level_3     = models.CharField(max_length=1000000)
    level_4     = models.CharField(max_length=1000000)
    level_5     = models.CharField(max_length=1000000)

    def __str__(self): 
        return self.level_1
    class Meta:
        verbose_name_plural = 'Keph_level'
        



class CompltHospCsv(models.Model):
    object_id                                   = models.IntegerField(primary_key=True)
    facility_n                                  = models.CharField(max_length=255)
    categories                                  = models.CharField(max_length=255)
    owner                                       = models.CharField(max_length=80, null=True)
    county                                      = models.CharField(max_length=80, null=True)
    sub_county                                  = models.CharField(max_length=80, null=True)
    division                                    = models.CharField(max_length=80, null=True)
    location                                    = models.CharField(max_length=80, null=True)
    sub_location                                = models.CharField(max_length=80, null=True)
    constituency                                = models.CharField(max_length=80, null=True)
    nearest_to                                  = models.CharField(max_length=80, null=True)
    Code                                        = models.IntegerField()
    Registration_number                         = models.IntegerField()
    Keph_level                                  = models.CharField(max_length=80, null=True) 
    Facility_type                               = models.CharField(max_length=80, null=True) 
    Owners                                      = models.CharField(max_length=80, null=True) 
    Regulatory_body                             = models.CharField(max_length=80, null=True) 
    Beds                                        = models.IntegerField()    
    Cots                                        = models.IntegerField()   
    Ward                                        = models.CharField(max_length=80, null=True)   
    Operation_status                            = models.CharField(max_length=80, null=True)  
    Open_whole_day                              = models.CharField(max_length=80, null=True) 
    Open_public_holidays                        = models.CharField(max_length=80, null=True)    
    Open_weekends                               = models.CharField(max_length=80, null=True)  
    Open_late_night                             = models.CharField(max_length=80, null=True)
    Approved                                    = models.CharField(max_length=80, null=True) 
    Public_visible                              = models.CharField(max_length=80, null=True)
    Closed                                      = models.CharField(max_length=80, null=True)
    latitude                                    = models.DecimalField(max_digits=30, decimal_places=12,default=0)
    longitude                                   = models.DecimalField(max_digits=30, decimal_places=12,default=0)
    # keph_level                                  = models.ForeignKey(KephLevel, on_delete=models.CASCADE, null=True)


    def __str__(self): 
        return self.facility_n
    class Meta:
        verbose_name_plural = 'CompltHospCsv'




