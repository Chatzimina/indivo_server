#chatzimina maria
from indivo.models import Fact
from django.db import models

class Seriousgames(Fact):
  createdAt = models.DateTimeField(null=True)
  extraWeapons =  models.CharField(max_length=200, null=True)
  name =  models.CharField(max_length=200, null=True)
  registerCode = models.CharField(max_length=20, null=True)
  registerEnabled =  models.CharField(max_length=20, null=True)
  supportEnabled =  models.CharField(max_length=20, null=True)
  userId =  models.CharField(max_length=50, null=True)
  registered =  models.CharField(max_length=50, null=True)


