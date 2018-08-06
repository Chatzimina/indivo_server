#chatzimina maria
from indivo.models import Fact
from django.db import models

class Procedure(Fact):
  date_performed = models.DateTimeField(null=True)
  name = models.CharField(max_length=800,null=True)
  name_type = models.CharField(max_length=800)
  name_value = models.CharField(max_length=800, null=True)
  name_abbrev = models.CharField(max_length=800, null=True)
  provider_name = models.CharField(max_length=800, null=True)
  provider_institution = models.CharField(max_length=200, null=True)
  location = models.CharField(max_length=100, null=True)
  comments = models.TextField(null=True)

