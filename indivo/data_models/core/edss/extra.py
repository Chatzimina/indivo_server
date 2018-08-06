from indivo.serializers import DataModelSerializers
from indivo.data_models.options import DataModelOptions
from indivo.lib.rdf import PatientGraph
from indivo.validators import ValueInSetValidator, ExactValueValidator, NonNullValidator

#SNOMED_URI = 'http://purl.bioontology.org/ontology/SNOMEDCT/'

class edssSerializers(DataModelSerializers):

    def to_rdf(queryset, result_count, record=None, carenet=None):
        if not record:
            record = carenet.record
        
        graph = PatientGraph(record)
        graph.addProblemList(queryset.iterator())
        return graph.toRDF()        

class edssOptions(DataModelOptions):
    model_class_name = 'edss'
    serializers = edssSerializers
    field_validators = {
        'date_performed': [NonNullValidator()],
        'visual': [NonNullValidator()],
        'brainstem': [NonNullValidator()],
        'pyramidal': [NonNullValidator()],
        'cerebellar': [NonNullValidator()],
        'sensory': [NonNullValidator()],
        'bladder': [NonNullValidator()],
        'cerebral': [NonNullValidator()],
        'ambulation': [NonNullValidator()],
         'score': [NonNullValidator()],
        }




  
 
  
