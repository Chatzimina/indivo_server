#chatzimina maria
from indivo.models import Fact
from indivo.fields import CodedValueField
from django.db import models
from indivo.fields import CodedValueField, ValueAndUnitField, PharmacyField, ProviderField

class Appointment(Fact):
  date = models.DateTimeField()
  time =  models.CharField(max_length=100)

  appointment_title = models.CharField(max_length=100)
  comments = models.TextField(null=True) 
  lastname = models.CharField(max_length=100,null=True)
  name = models.CharField(max_length=100,null=True)
  street_number = models.CharField(max_length=100,null=True)
  route = models.CharField(max_length=100,null=True)
  locality = models.CharField(max_length=500,null=True)
  postal_code = models.CharField(max_length=500,null=True)
  country = models.CharField(max_length=500,null=True)
  alert = models.CharField(max_length=500,null=True)
