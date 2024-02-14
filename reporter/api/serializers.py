from rest_framework import serializers
from ..models import (CompltHospCsv, HomaBayHospCsv, HbSubCounties, Hbschools, HbRoads, Homa_Bay, )



class CompltHospSerializer(serializers.ModelSerializer):
	created = serializers.SerializerMethodField()



	class Meta:
		model = CompltHospCsv
		fields	=(
				'object_id',                                  
			    'facility_n',                                 
			    'categories',                                  
			    'owner',                                      
			    'county',                                     
			    'sub_county',                                 
			    'division',                                   
			    'location',                                   
			    'sub_location',                                
			    'constituency',                                
			    'nearest_to',                                  
			    'Code',                                       
			    'Registration_number',                       
			    'Keph_level',                                
			    'Facility_type',                              
			    'Owners',                                      
			    'Regulatory_body',                            
			    'Beds',                                         
			    'Cots',                                         
			    'Ward',                                          
			    'Operation_status',                           
			    'Open_whole_day',                            
			    'Open_public_holidays',                          
			    'Open_weekends',                               
			    'Open_late_night',                           
			    'Approved',                                    
			    'Public_visible',                              
			    'Closed',                                     
			    'latitude',                                   
			    'longitude',)


		# def get_created(self, obj):
		# 	return obj.created.strftime('%Y-%m-%d %H:%M:%S')