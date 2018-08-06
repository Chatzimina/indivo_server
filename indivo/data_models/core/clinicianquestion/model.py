#chatzimina
from indivo.models import Fact
from django.db import models

class Clinicianquestion(Fact):
  patientName = models.CharField(max_length=200,null=True)
  patientId = models.CharField(max_length=200,null=True)
  diagnosisAge =  models.CharField(max_length=200,null=True)
  gender =  models.CharField(max_length=200,null=True)
  diagnosis = models.CharField(max_length=800,null=True)
  diagnosisExtra = models.CharField(max_length=800,null=True)
  initialDiagnosis = models.CharField(max_length=200,null=True)
  treatmentC = models.CharField(max_length=200,null=True)
  treatmentS = models.CharField(max_length=200,null=True)
  treatmentR = models.CharField(max_length=200,null=True)
  treatmentCI = models.CharField(max_length=200,null=True)
  treatmentSI = models.CharField(max_length=200,null=True)
  treatmentRI = models.CharField(max_length=200,null=True)
  treatmentCD = models.CharField(max_length=200,null=True)
  treatmentSD = models.CharField(max_length=200,null=True)
  treatmentRD = models.CharField(max_length=200,null=True)
  karnovskyIndex = models.CharField(max_length=200,null=True)
  expectedOutcome = models.CharField(max_length=200,null=True)
  computerSkills = models.CharField(max_length=200,null=True)
  computerGames = models.CharField(max_length=200,null=True)

