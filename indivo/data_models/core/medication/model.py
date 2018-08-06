#chatzimina maria
from indivo.models import Fact
from django.db import models
from indivo.fields import CodedValueField, ValueAndUnitField, PharmacyField, ProviderField

class Medication(Fact):
    drugName = CodedValueField()
    endDate = models.DateField(null=True)
    frequency = ValueAndUnitField()
    instructions = models.CharField(max_length=255, null=True)
    provenance = CodedValueField()
    quantity = ValueAndUnitField()
    startDate = models.DateField(null=True)
    drugNumber =  models.CharField(max_length=255, null=True)
    ingredients =  models.CharField(max_length=255, null=True)
    drugIntakes =  models.CharField(max_length=255, null=True)
    addingDate = models.DateTimeField(null=True)
    lastEditDate = models.DateTimeField(null=True)
    deletingEditDate = models.DateTimeField(null=True)
    deletingFeedback = models.CharField(max_length=255, null=True)

class Fill(Fact):
    date = models.DateTimeField(null=True)
    dispenseDaysSupply = models.FloatField(null=True)
    pbm = models.CharField(max_length=255, null=True)
    pharmacy = PharmacyField()
    provider = ProviderField()
    quantityDispensed = ValueAndUnitField()
    medication = models.ForeignKey(Medication, null=True, related_name='fulfillments')
  
