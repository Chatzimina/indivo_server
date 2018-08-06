"""
.. module:: views.sharing.shares_document
   :synopsis: Indivo view implementations related to sharing documents

.. moduleauthor:: Daniel Haas <daniel.haas@post.harvard.edu>
.. moduleauthor:: Ben Adida <ben@adida.net>

"""

import indivo.views
from indivo.lib.sharing_utils import carenet_documents_filter, document_in_carenet, document_carenets_filter
from indivo.views.base import *
from indivo.views.documents.document import _render_documents, _get_document, _render_document
from django.http import HttpResponseBadRequest
from django.core.exceptions import PermissionDenied

from django.db.models import F
from indivo.models import Document

from lxml import etree

from django.db.models.loading import get_model
from django.http import HttpResponseBadRequest, HttpResponse, Http404
from django.utils import simplejson

from indivo.lib.query import FactQuery
from indivo.lib.view_decorators import marsloader
from indivo.serializers.json import IndivoJSONEncoder
import json



# map request content types to Model serialization types
SERIALIZATION_FORMAT_MAP = {
    'application/json': 'json',
    'application/xml': 'xml',
    'text/xml': 'xml',
    'application/rdf+xml': 'rdf',
}



def serialize(cls, format, query, record=None, carenet=None):
    """Serialize an indivo.lib.query to the requested format

    Non-aggregate queries are handled by the data model's own serialization
    methods, while aggregate queries are serialized in a standard way to
    AggregateReports

    **Returns:**

    * A string representation of the serialized query results in the requested
      format

    """

    # aggregate queries
    if query.aggregate_by:
        return serialize_as_aggregate(format, query)

    # non-aggregate queries
    queryset = query.results
    result_count = query.trc
    method = "to_" + SERIALIZATION_FORMAT_MAP[format]
    if hasattr(cls, method):
        return getattr(cls, method)(queryset, result_count, record, carenet)
    else:
        raise ValueError("format not supported")



@transaction.commit_on_success
def carenet_document_placement(request, record, carenet, document_id):
  """ Place a document into a given carenet.

  Will return :http:statuscode:`200` on success, :http:statuscode:`404` if
  *document_id* doesn't exist or if *document_id* has a nevershare set
  on it.

  """

  document = _get_document(document_id=document_id, record=record)

  # don't allow this for nevershare documents
  if not document or document.nevershare:
    raise Http404

  CarenetDocument.objects.get_or_create(carenet=carenet, document=document)
  doc_share, created_p = CarenetDocument.objects.get_or_create(document = document, carenet = carenet, defaults={'share_p':True})


  doc_share.share_p = True
  doc_share.save()
  return DONE

def carenet_pha_placement(request, record, carenet, data_model):
  """ Place a document into a given carenet.

  Will return :http:statuscode:`200` on success, :http:statuscode:`404` if
  *document_id* doesn't exist or if *document_id* has a nevershare set
  on it.

  """
  
 
  query_params = {
         'status': 'active',
        }

  query_options=query_params

  response_format = request.GET.get("response_format", 'application/json')

  #data_model = pha.email.split("@")[0]
  model_class = get_model('indivo', data_model)

  if model_class is None:
      # model not found
      raise Http404
  
  limit=100
  offset = 0
  active_status = StatusName.objects.get(name='active')
    #status = request.GET.get('status', 'archived')
  query_params = {
         'limit': 200,
         'offset': 0,
         'order_by': None,
         'status': active_status,
         'aggregate_by': None, 'date_range': None, 'date_group': None, 'group_by': None,'filters': {}, 
         
        }
  carenetNone=None 
  model_filters =  model_class.filter_fields # TODO: possible to make a lazy class property?
  query = FactQuery(model_class,
                model_filters,
                query_params,
                record,
                carenetNone)

  try:
      query.execute()
      data = serialize(model_class, response_format, query, record, carenetNone)
#      return HttpResponse(data, mimetype=response_format) 
  except ValueError as e:
     return HttpResponseBadRequest(str(e))

  r = simplejson.loads(data)

  documents_ids=[]
  for i in r:

       documents_ids.append(i['__documentid__'])
  test=""

  for document_id in documents_ids:
   #  test+=j+","
  
   document = _get_document(document_id=document_id, record=record)

  # don't allow this for nevershare documents
   if not document or document.nevershare:
    raise Http404

   CarenetDocument.objects.get_or_create(carenet=carenet, document=document)
   doc_share, created_p = CarenetDocument.objects.get_or_create(document = document, carenet = carenet, defaults={'share_p':True})


   doc_share.share_p = True
   doc_share.save()
  return DONE


def carenet_pha_delete(request, record, carenet, data_model):
  """ Unshare all documents from a given carenet.

  If there is an autoshare of *document_id*'s type into *carenet*, this
  call creates an exception for *document_id* in *carenet*. If *document_id*
  was shared individually into *carenet*, this call removes it. If *document_id*
  is not shared in *carenet* at all, this call does nothing immediately.

  In all cases, this call exempts *document_id* from any future autoshares into
  this carenet.

  Will return :http:statuscode:`200` on success, :http:statuscode:`404` if
  *document_id* doesn't exist or if *document_id* or *carenet* don't belong
  to *record*.

  """
  response_format = request.GET.get("response_format", 'application/json')

  #data_model = pha.email.split("@")[0]
  model_class = get_model('indivo', data_model)

  if model_class is None:
      # model not found
      raise Http404

  limit=100
  offset = 0
  active_status = StatusName.objects.get(name='active')
    #status = request.GET.get('status', 'archived')
  query_params = {
         'limit': 200,
         'offset': 0,
         'order_by': None,
         'status': active_status,
         'aggregate_by': None, 'date_range': None, 'date_group': None, 'group_by': None,'filters': {},

        }
 # carenetNone=None
  model_filters =  model_class.filter_fields # TODO: possible to make a lazy class property?
  query = FactQuery(model_class,
                model_filters,
                query_params,
                record,
                carenet)

  try:
      query.execute()
      data = serialize(model_class, response_format, query, record, carenet)
#      return HttpResponse(data, mimetype=response_format)
  except ValueError as e:
     return HttpResponseBadRequest(str(e))
  
  r = simplejson.loads(data)

  documents_ids=[]
  for i in r:

       documents_ids.append(i['__documentid__'])
  test=""

  for document_id in documents_ids:

   document = _get_document(document_id=document_id, record=record)

   # this is always permission denied, so we can just handle it here
   # not in the access control system
   if not document or document.record != carenet.record:
    raise Http404

   doc_share, created_p = CarenetDocument.objects.get_or_create(document = document, carenet = carenet, defaults={'share_p':False})

   if not created_p: #and doc_share.share_p:

    doc_share.share_p = False
    doc_share.save()

  return DONE









def carenet_document_delete(request, carenet, record, document_id):
  """ Unshare a document from a given carenet.

  If there is an autoshare of *document_id*'s type into *carenet*, this 
  call creates an exception for *document_id* in *carenet*. If *document_id*
  was shared individually into *carenet*, this call removes it. If *document_id*
  is not shared in *carenet* at all, this call does nothing immediately.
  
  In all cases, this call exempts *document_id* from any future autoshares into
  this carenet.

  Will return :http:statuscode:`200` on success, :http:statuscode:`404` if 
  *document_id* doesn't exist or if *document_id* or *carenet* don't belong
  to *record*.

  """

  document = _get_document(document_id=document_id, record=record)

  # this is always permission denied, so we can just handle it here
  # not in the access control system
  if not document or document.record != carenet.record:
    raise Http404

  doc_share, created_p = CarenetDocument.objects.get_or_create(document = document, carenet = carenet, defaults={'share_p':False})

  if not created_p: #and doc_share.share_p:

    doc_share.share_p = False
    doc_share.save()

  return DONE


def carenet_record(request, carenet):
  """ Get basic information about the record to which a carenet belongs.

  For now, info is the record id, label, creation time, creator, contact,
  and demographics.

  Will return :http:statuscode:`200` with XML about the record on success.

  """
  return render_template('record', {'record': carenet.record})


@marsloader()
def carenet_document_list(request, carenet, query_options):
  """List documents from a given carenet.

  request.GET may contain:
  
  * *type*: The document schema type to filter on.

  Returns both documents in the given carenet and documents with the same types 
  as in the record's autoshare, filtered by *type* if passed.

  Will return :http:statuscode:`200` with a document list on success,
  :http:statuscode:`404` if *type* doesn't exist.

  """
  
  try:
    doc_type_uri = request.GET.get('type', None)
    if doc_type_uri:
      requested_doc_type = DocumentSchema.objects.get(type = doc_type_uri)
    else:
      requested_doc_type = None
  except DocumentSchema.DoesNotExist:
    raise Http404

  documents = carenet_documents_filter(carenet, carenet.record.documents)
  tdc = documents.count()

  offset = query_options['offset']
  limit = query_options['limit']
  ret_documents = documents[offset:offset+limit]

  return _render_documents(ret_documents, carenet.record, None, tdc)



def carenet_document(request, carenet, document_id):
  """Return a document from a carenet.

  Will only return the document if it exists within the carenet.
  
  Will return :http:statuscode:`200` with the document content on success,
  :http:statuscode:`404` if *document_id* is invalid or if the indicated
  document is not shared in *carenet*.

  """
  
  document = _get_document(document_id=document_id, carenet=carenet)
  if not document or document.nevershare:
    raise Http404

  if document_in_carenet(carenet, document_id):
    return _render_document(document)
  else: 
    raise Http404

def document_carenets(request, record, document_id):
  """List all the carenets into which a document has been shared.

  Will return :http:statuscode:`200` with a list of carenets on success,
  :http:statuscode:`404` if *document_id* is invalid.
  
  """
  document = _get_document(document_id=document_id, record=record)
  if not document:
    raise Http404

  # Get the carenets
  carenets = document_carenets_filter(document, Carenet.objects.all())

  return render_template('carenets', {'carenets' : carenets, 'record' : record})
