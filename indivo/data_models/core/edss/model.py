#chatzimina maria
from indivo.models import Fact
from django.db import models

class edss(Fact):
  date_performed = models.DateTimeField(null=True)
  visual  = models.CharField(max_length=1000)
  visualDe  = models.CharField(max_length=1000)
  brainstem  = models.CharField(max_length=1000, null=True)
  brainstemDe  = models.CharField(max_length=1000, null=True)
  pyramidal = models.CharField(max_length=1000, null=True)
  pyramidalDe = models.CharField(max_length=1000, null=True)
  cerebellar = models.CharField(max_length=1000, null=True)
  cerebellarDe = models.CharField(max_length=1000, null=True)
  sensory = models.CharField(max_length=1000, null=True)
  sensoryDe = models.CharField(max_length=1000, null=True)
  bladder = models.CharField(max_length=1000, null=True)
  bladderDe = models.CharField(max_length=1000, null=True)
  doctor_name = models.CharField(max_length=1000, null=True)
  cerebral = models.CharField(max_length=1000, null=True)
  cerebralDe = models.CharField(max_length=1000, null=True)
  ambulation =  models.CharField(max_length=1000, null=True)
  ambulationDe = models.CharField(max_length=1000, null=True)
  score =  models.CharField(max_length=1000, null=True)
  comments = models.TextField(null=True)
  


