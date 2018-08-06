from indivo.serializers import DataModelSerializers
from indivo.data_models.options import DataModelOptions
from indivo.lib.rdf import PatientGraph
from indivo.validators import ValueInSetValidator, ExactValueValidator, NonNullValidator

SNOMED_URI = 'http://purl.bioontology.org/ontology/SNOMEDCT/'

class SeriousgamesSerializers(DataModelSerializers):

    def to_rdf(queryset, result_count, record=None, carenet=None):
        if not record:
            record = carenet.record
        
        graph = PatientGraph(record)
        graph.addProblemList(queryset.iterator())
        return graph.toRDF()        

class SeriousgamesOptions(DataModelOptions):
    model_class_name = 'Seriousgames'
    serializers = SeriousgamesSerializers
    field_validators = {

        'name' : [NonNullValidator()],#ExactValueValidator(SNOMED_URI)],
#        'name_type': [NonNullValidator()],
 #       'name_value': [NonNullValidator()],
#       'name_abbrev': [NonNullValidator()],
#        'provider_name' : [NonNullValidator()],
#        'location': [NonNullValidator()],
#        'comments':[NonNullValidator()],
        }




  
 
  
