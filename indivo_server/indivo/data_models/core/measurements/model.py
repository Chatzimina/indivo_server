#chatzmina
from indivo.models import Fact
from django.db import models

class Measurements(Fact):
  
  name = models.CharField(max_length=100)
  name_value = models.CharField(max_length=100, null=True)
  name_abbrev =  models.CharField(max_length=100, null=True)
  number = models.CharField(max_length=200, null=True)
  kind = models.CharField(max_length=200, null=True)
  value = models.CharField(max_length=200, null=True)
  unit = models.CharField(max_length=100, null=True)
  comments = models.TextField(null=True)
  measurementDate =  models.DateTimeField(null=True)

