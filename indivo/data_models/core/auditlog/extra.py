from indivo.serializers import DataModelSerializers
from indivo.validators import ValueInSetValidator, ExactValueValidator, NonNullValidator
from indivo.data_models.options import DataModelOptions
from indivo.lib.rdf import PatientGraph

valid_app_name = [
    'myhealthavatar',
    'games_for_kids',
    'games_for_adults',
    'imanagemyhealth',
    'isupportmypatients',
    'imcportal',
]

valid_country = [
    'germany',
    'italy',
    'uk',
]

class AuditlogSerializers(DataModelSerializers):
    def to_rdf(queryset, result_count, record=None, carenet=None):
        if not record:
            record = carenet.record
        
        graph = PatientGraph(record)
        graph.addAuditlogList(queryset.iterator())
        return graph.toRDF()

class AuditlogOptions(DataModelOptions):
    model_class_name = 'auditlog'
    serializers = AuditlogSerializers
    field_validators = {
#        'app_name': [ValueInSetValidator(valid_app_name, nullable=False)],
#        'country': [ValueInSetValidator(valid_country, nullable=True)],
        }
