"""
.. module: views.record
   :synopsis: Indivo view implementations for record-related calls.

.. moduleauthor:: Daniel Haas <daniel.haas@post.harvard.edu>
.. moduleauthor:: Ben Adida <ben@adida.net>

"""

#import libxml2
from lxml import etree

from indivo.lib import utils
from indivo.views.documents.document import _document_create
from base import *
import json
from django.db.models import Q
import psycopg2
import requests

from indivo.views.documents.document import _get_document
from indivo.lib import iso8601
import base64, hmac, datetime

from django.utils import simplejson
from oauth.djangoutils import extract_request


ACTIVE_STATE = 'active'



@marsloader()
def record_list(request, account, query_options):
  """ List all available records for an account.

  This includes records that *account* owns, records that have been fully shared
  with *account*, and records that are shared with *account* via carenets.

  Will return :http:statuscode:`200` with a list of records on success.

  """

  json = request.GET.get('json', None)

  
  records = account.records_owned_by.all()
  full_shares = account.fullshares_to.all()
  carenet_shares = account.carenetaccount_set.all()

  if json == 'yes':
      return render_template('record_list', {'records': records, 'full_shares' : full_shares, 'carenet_shares': carenet_shares}, type='json')
  return render_template('record_list', {'records': records, 'full_shares' : full_shares, 'carenet_shares': carenet_shares}, type='xml')


def record_get_owner(request, record):
  """ Get the owner of a record.

  Will always return :http:statuscode:`200`. The response body will contain the
  owner's email address, or the empty string if the record is unowned.
  
  """

  owner_email = ""
  if record.owner:
    owner_email = record.owner.email
  return render_template('account_id', {'id': owner_email})


def record_set_owner(request, record):
  """ Set the owner of a record.

  request.POST must contain the email address of the new owner.

  Will return :http:statuscode:`200` with information about the new
  owner on success, :http:statuscode:`400` if request.POST is empty
  or the passed email address doesn't correspond to an existing principal.
  
  """



  try:
               conn = psycopg2.connect("dbname='indivo' user='indivo' host='localhost' password='indivo'")
#               conn.autocommit = True
               conn.set_isolation_level(0)
               conn.commit()
               cursor = conn.cursor()

  except psycopg2.DatabaseError, e:
                   existing_account_i="Cannot connect to db"



  try:

                   cursor.execute( "SELECT account_id FROM indivo_account where contact_email='"+request.raw_post_data+"'" )
                   conn.commit()
                   result = cursor.fetchall()

  except psycopg2.DatabaseError, e:
                   url=e
                   if conn:
                        conn.rollback()

                        print 'Error %s' % e

  if result:
     try:

                   cursor.execute( "SELECT username FROM indivo_accountauthsystem where account_id='"+str(result[0][0])+"'" )
                   conn.commit()
                   username = cursor.fetchall()

     except psycopg2.DatabaseError, e:
                   url=e
                   return HttpResponse(e)
                   if conn:
                        conn.rollback()

                        print 'Error %s' % e

     if username:
      url='https://www.iphr.care:8004/registration.php?username='+username[0][0]+'&record='+record.id #forum
      r = requests.post(url)
  try:
    record.owner = Principal.objects.get(email=request.raw_post_data)
    record.save()
  except Principal.DoesNotExist:
    logging.error('Post has no owner in body')
    return HttpResponseBadRequest()
  return render_template('account', {'account': record.owner})
    

def record(request, record):
  """ Get information about an individual record.

  Will return :http:statuscode:`200` with information about the record on
  success.

  """

  return render_template('record', {'record': record})

def record_search(request):
  """ Search for records by label (usually the same as full name).

  request.GET must contain the query parameters, any of:

  * *label*: The record's label

  This call returns all records matching any part of any of the 
  query parameters: i.e. it ORs together the query parameters and
  runs a partial-text match on each.

  Will return :http:statuscode:`200` with XML describing matching
  records on success, :http:statuscode:`400` if no query parameters 
  are passed.

  """

  label = request.GET.get('label', None)

  if not label:
    return HttpResponseBadRequest('No search criteria given')

  query_filter = Q()
  if label:
    query_filter |= Q(label__icontains=label)

  query = Record.objects.filter(query_filter)

  return render_template('record_list', {'records':query}, type='xml')
                                         
@utils.django_json
def record_phas(request, record):
  """ List userapps bound to a given record.

  request.GET may optionally contain:

  * *type*: An XML schema namespace. If specified, only apps which
    explicitly declare themselves as supporting that namespace will
    be returned.

  Will return :http:statuscode:`200` with a list of JSON manifests
  for the matching apps on success.

  """

  phas = record.phas

  # are we filtering by schema?
  type = request.GET.get('type', None)
  if type:
    schema = DocumentSchema.objects.get(type=type)
    phas = [pha for pha in phas if pha.schema == schema]

  # interpolate the the start_url_template into start_url
  manifests = []
  newlist = sorted(phas, key=lambda x: x.name, reverse=False)
  for pha in newlist:
   # return ("{'name':'"+pha.name+"'}")

    pha.start_url = utils.url_interpolate(pha.start_url_template, {'record_id' : record.id})
    manifests.append(pha.to_manifest(as_string=False))

  return manifests

@utils.django_json
def record_pha(request, record, pha):
  """ Get information about a given userapp bound to a record.

  Will return :http:statuscode:`200` with a JSON manifest for the app on success,
  :http:statuscode:`404` if the app isn't actually bound to the record.

  """

  try:
    pha = record.pha_shares.get(with_pha__email = pha.email).with_pha
  except PHAShare.DoesNotExist:
    raise Http404
  pha.start_url = utils.url_interpolate(pha.start_url_template, {'record_id' : record.id})
  return pha.to_manifest(as_string=False)


def record_notify(request, record):
  """ Send a notification about a record to all accounts authorized to be notified.

  Notifications should be short alerts, as compared to full inbox messages, and
  may only be formatted as plaintext.

  request.POST must contain:

  * *content*: The plaintext content of the notification.

  request.POST may contain:

  * *document_id*: The document to which this notification pertains.

  * *app_url*: A callback url to the app for more information.

  Will return :http:statuscode:`200` on success, :http:statuscode:`400` if 
  *content* wasn't passed.

  """

  CONTENT = 'content'
  if request.POST.has_key(CONTENT):
    content = request.POST[CONTENT]
    record.notify(request.principal.effective_principal, 
                  content     = content, 
                  document_id = request.POST.get('document_id', None), 
                  app_url     = request.POST.get('app_url', None))
    # return the notification ID instead of DONE?
    return DONE
  else:
    return HttpResponseBadRequest()


def record_shares_companion(request, record):

  try:
               conn = psycopg2.connect("dbname='indivo' user='indivo' host='localhost' password='indivo'")
               #conn.autocommit = True
               conn.set_isolation_level(0)
               conn.commit()
               cursor = conn.cursor()

  except psycopg2.DatabaseError, e:
                 print "Cannot connect to db"

  try:
               cursor.execute("SELECT with_account_id FROM indivo_accountfullshare where record_id='" +record.id+"'")
               results = cursor.fetchall()
  except psycopg2.DatabaseError, e:

               if conn:
                 conn.rollback()
                 return HttpResponse(e)
                 print 'Error %s' % e
  resultname =[]

  for h in results:
    try:
               cursor.execute("SELECT  full_name, contact_email FROM indivo_account where account_id='" +str(h[0])+"'")
               resultname.append(cursor.fetchall())

    except psycopg2.DatabaseError, e:

               if conn:
                 conn.rollback()
                 return HttpResponse(e)
                 print 'Error %s' % e

  data = []
  for res in resultname:
        for r in res:

                data.append({'name':r[0],'email':r[1]})



  results = json.dumps(data)
  return HttpResponse(results)




def record_shares(request, record):
  """ List the shares of a record.

  This includes shares with apps (phashares) and full shares with accounts
  (fullshares).
  
  Will return :http:statuscode:`200` with a list of shares on success.

  """

  pha_shares = record.pha_shares.all()
  full_shares = record.fullshares.all()
  return render_template('shares', {'fullshares': full_shares, 'phashares':pha_shares, 'record': record})


def record_share_add(request, record):
  """ Fully share a record with another account.

  A full share gives the recipient account full access to all data and apps 
  on the record, and adds the recipient to the list of accounts who are alerted
  when the record gets a new alert or notification.

  request.POST must contain:

  * *account_id*: the email address of the recipient account.

  request.POST may contain:

  * *role_label*: A label for the share (usually the relationship between the
    record owner and the recipient account, i.e. 'Guardian')

  Will return :http:statuscode:`200` on success, :http:statuscode:`400` if
  *account_id* was not passed, and :http:statuscode:`404` if the passed
  *account_id* does not correspond to an existing Account.

  """

  ACCOUNT_ID = 'account_id'
  try:
    if request.POST.has_key(ACCOUNT_ID):
      other_account_id = request.POST[ACCOUNT_ID].lower().strip()
      account = Account.objects.get(email=other_account_id)
      RecordNotificationRoute.objects.get_or_create(account = account, record = record)
      share = AccountFullShare.objects.get_or_create(record = record, with_account = account, role_label = request.POST.get('role_label', None))
      return DONE
    else:
      return HttpResponseBadRequest()
  except Account.DoesNotExist:
    raise Http404
  except Principal.DoesNotExist:
    raise Http404


def record_share_delete(request, record, other_account_id):
  """ Undo a full record share with an account.
  
  Will return :http:statuscode:`200` on success, :http:statuscode:`404` if
  *other_account_id* doesn't correspond to an existing Account.

  """

  try:
    shares = AccountFullShare.objects.filter(record = record, with_account = Account.objects.get(email=other_account_id.lower().strip()))
    shares.delete()
    return DONE
  except Account.DoesNotExist:
    raise Http404
  except Principal.DoesNotExist:
    raise Http404

@transaction.commit_on_success
def record_create(request, principal_email=None, external_id=None):
  """ Create a new record.

  For 1:1 mapping of URLs to views: just calls 
  :py:meth:`~indivo.views.record._record_create`.

  """
  
  return _record_create(request, principal_email, external_id)

@transaction.commit_on_success
def record_create_ext(request, principal_email=None, external_id=None):
  """ Create a new record with an associated external id.

  For 1:1 mapping of URLs to views: just calls 
  :py:meth:`~indivo.views.record._record_create`.

  """

  return _record_create(request, principal_email, external_id)

def _record_create(request, principal_email=None, external_id=None):
  """ Create an Indivo record.

  request.POST must contain raw XML that is a valid Indivo Demographics
  document (see :doc:`/schemas/demographics-schema`).
  
  This call will create a new record containing the following 
  information:

  * *creator*: Corresponds to ``request.principal``.

  * *label*: The full name of the new record, specified in the
    demographics document.

  * *owner*: Corresponds to ``request.principal``.

  * *external_id* An external identifier for the record, if 
    passed in.

  Additionally, this call will create a Demographics document for the record.

  Will return :http:statuscode:`200` with information about the record on
  success, :http:statuscode:`400` if the demographics data in request.POST was
  empty or invalid XML.
  
  """

  # If the xml data is not valid return an HttpResponseBadRequest Obj
  xml_data = request.raw_post_data
  root_temp = etree.XML(xml_data) 

  try:
            with open(('/media/data/hatzimin/web/indivo_server/indivo/schemas/data/core/demographics/schema.xsd'), 'r') as schema_file:
                schema = etree.XMLSchema(etree.parse(schema_file))
            schema.assertValid(root_temp)
  except etree.DocumentInvalid as e:
        return HttpResponseBadRequest("Demographics XML not valid based on indivo model schema.Input document didn't validate, error was: %s"%(str(e)))



  try:
    etree.XML(xml_data)
  except:
    return HttpResponseBadRequest("Demographics XML not valid")

  demographics = Demographics.from_xml(xml_data)
  label = demographics.name_given + ' ' + demographics.name_family

  record_external_id = Record.prepare_external_id(external_id, principal_email)
    
  if external_id:
    record , created_p = Record.objects.get_or_create(
      external_id = record_external_id,
      defaults = {
        'creator' : request.principal,
        'label' : label,
        'owner' : request.principal})
  else:
    record = Record.objects.create(
      external_id = record_external_id,
      creator = request.principal,
      label = label,
      owner = request.principal)
    created_p = True

  # only set up the new demographics document if the record is new
  # otherwise just return the existing record
  if created_p:
    # Create default carenets for this particular record
    record.create_default_carenets()

    # Create the demographics document
    # use the same external ID as for the record
    # since those are distinct anyways
    doc_external_id = record_external_id

    doc = _document_create( record      = record,
                            creator     = request.principal,
                            pha         = None,
                            content     = xml_data,
                            external_id = doc_external_id)
      
    # set up demographics model and add it to the record
    demographics.document = doc
    demographics.save()
    record.demographics = demographics
    record.save()

    #import subprocess
    #stri=str("python /media/data/hatzimin/web/enableapps.py "+record.id)

    #subprocess.call(stri, shell=True)

#    return HttpResponse(subprocess.check_output(stri, shell=True))
#    headersAdmin={'IMC-TOKEN':'1d430b8a8da9c50a6dbd','ADMIN':''}

#    url='https://www.iphr.care:443/api/records/'+record.id+'/apps/allergies@apps.indivo.org/setup'

#    r=requests.post(url,headers=headersAdmin,verify=True)
#    return HttpResponse(r.text)
  #  headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

   # r=requests.get('https://www.iphr.care/enableapps/?record_id='+record.id,headers=headers,verify=True) 
#    return HttpResponse(r)
#    url='https://www.iphr.care/enableapps/?record_id='+record.id
#    r = requests.post(url,verify=True)
#    return HttpResponse(record.id)
  return render_template('record', {'record' : record}, type='xml')

@transaction.commit_on_success
def record_pha_setup(request, record, pha):
  """ Bind an app to a record without user authorization.

  This call should be used to set up new records with apps required
  for this instance of Indivo to run (i.e. syncer apps that connect to 
  data sources). It can only be made by admins, since it skips the
  normal app authorization process.

  ``request.POST`` may contain raw content that will be used
  as a setup document for the record.

  Will return :http:statuscode:`200` with a valid access token for the
  app bound to the record on success.
  
  """

  # TODO: eventually, when there are permission restrictions on a PHA, 
  # make sure that any permission restrictions on the current PHA are 
  # transitioned accordingly.

  content = request.raw_post_data

  # if there is a document, create it
  if content:
    # is there already a setup doc
    setup_docs = Document.objects.filter(record=record, pha=pha, external_id='SETUP')
    if len(setup_docs) == 0:
      new_doc = _document_create( record      = record,
                                  creator     = request.principal,
                                  pha         = pha,
                                  content     = content,
                                  external_id = Document.prepare_external_id('SETUP', pha, pha_specific=True, record_specific=True))


 
 
 # if cust == 'yes':
 
  # preauthorize the token.
  from indivo.accesscontrol.oauth_servers import OAUTH_SERVER
  access_token = OAUTH_SERVER.generate_and_preauthorize_access_token(pha, record=record)

  # return the token
  return HttpResponse(access_token.to_string(), mimetype="application/x-www-form-urlencoded")
