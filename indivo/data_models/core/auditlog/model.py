#chatzimina
from indivo.models import Fact
from django.db import models
from indivo.fields import CodedValueField, QuantitativeResultField, OrganizationField, NameField
from datetime import datetime

class Auditlog(Fact):

#    app_name_choices = ( 
#	('myhealthavatar', 'myhealthavatar'), 
#	('game_for_kids', 'game_for_kids'),
#	('game_for_adults','game_for_adults'),
#	('imanagemyhealth','imanagemyhealth'),
#        ('iManageMyHealth','imanagemyhealth'),
#	('isupportmypatients','isupportmypatients'),
#	('imcportal','imcportal'), 
#        ('mha_for_imc_app','mha_for_imc_app'),

#	)
 #   country_choices =(
#	('italy','italy'),
#	('germany','germany'),
#	('uk','uk'),
#	)


    app_name =  models.CharField(max_length=255, null=False)#, choices=app_name_choices)
    app_module =  models.CharField(max_length=255, null=True)
    event_name =  models.CharField(max_length=255, null=True)
    event_parameters =  models.CharField(max_length=255, null=True)
    patient =  models.CharField(max_length=255, null=False)
    country =  models.CharField(max_length=255, null=True)#, choices=country_choices)
    timestamp =  models.DateTimeField(default=datetime.now, null=True)
    flag = models.IntegerField(null=True)

