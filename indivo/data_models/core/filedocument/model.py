#chatzimina maria
from indivo.models import Fact
from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import uuid


fs = FileSystemStorage(location=settings.MEDIA_ROOT+'/documents_app/')
filename=uuid.uuid4()

class Filedocument(Fact):

  type_choices = (
        ('laboratory', 'laboratory'),
        ('finding', 'finding'),
        ('discharge','discharge'),
        ('other','other'),
        )



  registered_date = models.DateTimeField(null=True)
  title = models.CharField(max_length=800,null=True)
  file_id = models.CharField(max_length=800,null=True)
  file_set_id = models.CharField(max_length=800,null=True)
  type_of_file = models.CharField(max_length=800,null=True, choices = type_choices)
  filename = models.CharField(max_length=800)
  file_base64= models.TextField(null=True)
#  base64 = BinaryField()#models.CharField(max_length=100000000,null=True)
#  diagnosis22 = models.CharField(max_length=800,null=True)
  file = models.FileField(storage=fs,upload_to=filename,null=True)
  organisation = models.CharField(max_length=800,null=True)
  doctor = models.CharField(max_length=800,null=True)
  diagnosis = models.CharField(max_length=800,null=True)
  reasons = models.CharField(max_length=800,null=True)
  comments = models.TextField(null=True)

