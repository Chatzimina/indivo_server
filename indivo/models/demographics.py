"""
Indivo Model for Demographics
"""
import os
from django.conf import settings
from lxml import etree

from django.db import models
from django.core import serializers
from django.utils import simplejson
from django.http import HttpResponse
import logging, copy,string


from base import BaseModel, DataModelBase
from indivo.fields import AddressField, NameField, TelephoneField
from indivo.lib.iso8601 import parse_utc_date 
from indivo.lib.rdf import PatientGraph
from indivo.serializers.json import IndivoJSONEncoder

FIELDS = ('bday', 
          'email', 
          'ethnicity', 
          'gender', 
          'preferred_language', 
          'race', 
          'name_given', 
          'name_suffix',
          'name_middle',
          'name_family', 
          'name_prefix', 
          'tel_2_type', 
          'tel_2_preferred_p', 
          'tel_2_number', 
          'adr_region', 
          'adr_country', 
          'adr_postalcode', 
          'adr_city', 
          'adr_street', 
          'tel_1_type', 
          'tel_1_preferred_p', 
          'tel_1_number',
	  'siop',
          'weight',
          'weight_unit',
          'age',
          'pregnancy',
          'smoking'

          )

class Demographics(BaseModel):
    """ SMART style demographics """
    __metaclass__ = DataModelBase
    
    created_at = models.DateTimeField(auto_now_add = True)
    document = models.ForeignKey('Document', null=True)
    
    adr = AddressField()
    bday = models.DateField()
    email = models.CharField(max_length=200, null=True)
    ethnicity = models.CharField(max_length=200, null=True)
    gender = models.CharField(max_length=50)
    name = NameField()
    preferred_language = models.CharField(max_length=200, null=True)
    race = models.CharField(max_length=200, null=True)
    tel_1 = TelephoneField()
    tel_2 = TelephoneField()
    siop = models.CharField(max_length=200, null=True)
    pregnancy =  models.CharField(max_length=200, null=True)
    weight =  models.CharField(max_length=200, null=True)
    weight_unit =  models.CharField(max_length=200, null=True)
    smoking =  models.CharField(max_length=200, null=True)
    

    @classmethod
    def from_xml(klass, xml):
        attrs = {}
        _tag = lambda tag_name: "{%s}%s"%("http://indivo.org/vocab/xml/documents#", tag_name)
        
        # build etree
        try:
            root = etree.XML(xml)
            logging.debug("ROOT_mariaaaaaaa%s",str(xml))
        except Exception as e:
            raise ValueError("Input document didn't parse as XML, error was: %s"%(str(root)))
 
        root_temp = etree.XML(xml)
        for child in root_temp:
          if child.tag != "{http://indivo.org/vocab/xml/documents#}weight":
             test='' 
          else:# TODO: do your check here!
            root_temp.remove(child)
 
          if child.tag != "{http://indivo.org/vocab/xml/documents#}weight_unit":
            test=''
          else:# TODO: do your check here!
            root_temp.remove(child)
          if child.tag != "{http://indivo.org/vocab/xml/documents#}pregnancy":
            test=''
          else:# TODO: do your check here!
            root_temp.remove(child)
          if child.tag != "{http://indivo.org/vocab/xml/documents#}smoking":
            test=''
          else:# TODO: do your check here!
            root_temp.remove(child)







 
        # validate XML
        try:
            with open(os.path.join(settings.APP_HOME, 'indivo/schemas/data/core/demographics/schema.xsd'), 'r') as schema_file:
                schema = etree.XMLSchema(etree.parse(schema_file))
      
       
            schema.assertValid(root_temp)
        except etree.DocumentInvalid as e:
            raise ValueError("Input document didn't validate, error was: %s"%(str(e)))
  
        # parse XML
        attrs['bday'] = parse_utc_date(root.findtext(_tag('dateOfBirth')))
        attrs['gender'] = root.findtext(_tag('gender'))
        attrs['email'] = root.findtext(_tag('email'))
        attrs['ethnicity'] = root.findtext(_tag('ethnicity'))
        attrs['race'] = root.findtext(_tag('race'))
        attrs['preferred_language'] = root.findtext(_tag('preferredLanguage'))
        attrs['siop'] = root.findtext(_tag('siop'))
        attrs['pregnancy'] = root.findtext(_tag('pregnancy'))
        attrs['weight'] = root.findtext(_tag('weight'))
        attrs['weight_unit'] = root.findtext(_tag('weight_unit'))
        attrs['smoking'] = root.findtext(_tag('smoking'))



        nameElement = root.find(_tag('Name'))
        attrs['name_family'] = nameElement.findtext(_tag('familyName'))
        attrs['name_given'] = nameElement.findtext(_tag('givenName'))
        attrs['name_middle'] = nameElement.findtext(_tag('middleName'))
        attrs['name_prefix'] = nameElement.findtext(_tag('prefix'))
        attrs['name_suffix'] = nameElement.findtext(_tag('suffix'))
        
        telephoneElements = root.findall(_tag('Telephone'))
        if len(telephoneElements) > 0:
            tel_1 = telephoneElements[0]
            attrs['tel_1_type'] = tel_1.findtext(_tag('type'))
            attrs['tel_1_number'] = tel_1.findtext(_tag('number'))
            attrs['tel_1_preferred_p'] = 'false' != tel_1.findtext(_tag('preferred'))
            
        if len(telephoneElements) > 1:
            tel_2 = telephoneElements[1]
            attrs['tel_2_type'] = tel_2.findtext(_tag('type'))
            attrs['tel_2_number'] = tel_2.findtext(_tag('number'))
            attrs['tel_2_preferred_p'] = 'false' !=  tel_2.findtext(_tag('preferred'))
        
        addressElement = root.find(_tag('Address'))
        if addressElement is not None:
            attrs['adr_country'] = addressElement.findtext(_tag('country'))
            attrs['adr_city'] = addressElement.findtext(_tag('city'))
            attrs['adr_postalcode'] = addressElement.findtext(_tag('postalCode'))
            attrs['adr_region'] = addressElement.findtext(_tag('region'))
            attrs['adr_street'] = addressElement.findtext(_tag('street'))
        
        return klass(**attrs)
        
    def uri(self):
        return "http://indivo.org/records/%s/demographics"%(self.record.id)
        
    def as_json(self):
        """JSON string representation of Demographics instance"""
        data = serializers.serialize("indivo_python", [self], fields=FIELDS)
        return simplejson.dumps(data, cls=IndivoJSONEncoder)
    
    def as_xml(self):
        """XML string representation of Demographics instance"""
        root = serializers.serialize("indivo_xml", [self], fields=FIELDS)
        return etree.tostring(root)
    
    def as_rdf(self):
        """RDF/XML string representation of Demographics instance"""
        graph = PatientGraph(self.record)
        graph.addDemographics(self.record)
        return graph.toRDF()
    
