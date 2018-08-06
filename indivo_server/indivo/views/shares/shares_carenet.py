"""
.. module:: views.sharing.shares_carenet
   :synopsis: Indivo view implementations related to carenet management.

.. moduleauthor:: Daniel Haas <daniel.haas@post.harvard.edu>
.. moduleauthor:: Ben Adida <ben@adida.net>

"""

from indivo.views.base import *
from django.http import HttpResponseBadRequest
from django.core.exceptions import PermissionDenied
from django.db import IntegrityError
import psycopg2
from django.db.models import Q
import requests
import certifi
import json

NAME = 'name'



@transaction.commit_on_success
def carenet_create(request, record):
    """ Create a new carenet for a record.
  
    request.POST must contain:
    
    * *name*: the label for the new carenet.

    Will return :http:statuscode:`200` with XML describing the new
    carenet on success, :http:statuscode:`400` if *name* wasn't passed
    or if a carenet named *name* already exists on this record.
    
    """

    if request.POST.has_key(NAME):
        carenet_name = request.POST[NAME]
        try:
            cnObj = Carenet.objects.create(name = carenet_name, record = record)
        except IntegrityError:
            transaction.rollback()
            return HttpResponseBadRequest('Carenet name is already taken')
        return render_template('carenets', {'carenets':[cnObj], 'record':record}, type="xml")
    return HttpResponseBadRequest('Please provide a name for the carenet')


def carenet_list(request, record):
    """ List all carenets for a record.

    Will return :http:statuscode:`200` with a list of carenets on success.

    """
    json_att = request.GET.get('json',None)
    username = request.GET.get('username', None)
    record_id = str(record).split(' ')[1]
    carenets = Carenet.objects.filter(record=record)

    result = '' 
    accounts = []
    contact_emails = []
    if username == 'yes':

       try:
          conn = psycopg2.connect("dbname='indivo' user='indivo' host='localhost' password='indivo'");
#          conn.autocommit = True
          conn.set_isolation_level(0)
          conn.commit()
          cursor = conn.cursor()

       except psycopg2.DatabaseError, e:
           return HttpResponse(e)
           print 'Error %s' % e

       try:

          cursor.execute("SELECT id FROM indivo_carenet where record_id="+"'"+record_id+"'")
          conn.commit()
          result = cursor.fetchall()


       except psycopg2.DatabaseError, e:
         return HttpResponse(e)
         if conn:
            conn.rollback()

       if result != ' ':
         for i in result:
           try:

             cursor.execute("SELECT account_id FROM indivo_carenetaccount where carenet_id="+"'"+i[0]+"'")
             conn.commit()
             account  = cursor.fetchall()
             for m in account:
                accounts.append(m)
           except psycopg2.DatabaseError, e:
              return HttpResponse(e)
      
         for account_id in accounts:

          if account_id != '':
            try:

              cursor.execute("SELECT contact_email FROM indivo_account where account_id="+"'"+account_id[0]+"'")
              conn.commit()
              result_ = cursor.fetchall()
              contact_emails.append(result_[0][0])

            except psycopg2.DatabaseError, e:
              return HttpResponse(e)
	    try:

              cursor.execute("SELECT token FROM indivo_sessiontoken where user_id="+"'"+account_id[0]+"'ORDER BY expires_at DESC LIMIT 1")
              conn.commit()
              token_result = cursor.fetchall()


            except psycopg2.DatabaseError, e:
              return HttpResponse(e)

	    url = 'https://www.iphr.care:443/oauth2/access_token'
            r = requests.post(url,data='client_id=38525ae9102bb34a72ab&client_secret=c4ca8bd3eb7109718380104b1b5bcab9fd45c267&grant_type=password&username=jsmith&password=password.example',verify=True)

            data = json.loads(r.text)
            token_resul=data['access_token']


            headersAdmin={'IMC-TOKEN':str(token_resul),'ADMIN':''}

            r=' '
            for contact_email in contact_emails:
  
              url = 'https://www.iphr.care/api/accounts/'+contact_email+'?json=yes'
              res= requests.get(url,headers=headersAdmin,verify=True)    
              r += res.text
            tmpString ='{"Accounts":['


            tmpString += r.replace("}\n{","},{")
            tmpString +='] }'
            if json_att == 'yes':
              return HttpResponse(tmpString,content_type='application/json')
            return HttpResponse(tmpString,content_type='application/json')
#            query_filter = Q()

#            if contact_email:
#               query_filter |= Q(contact_email__icontains = contact_email)

 #              query = Account.objects.filter(query_filter)
               
 #              return render_template('accounts_search', {'accounts': query}, type='json')
            



    if json_att == 'yes':
        return render_template('carenets', {'carenets':carenets, 'record':record}, type="json")
    return render_template('carenets', {'carenets':carenets, 'record':record}, type="xml")


def carenet_delete(request, carenet):
    """ Delete a carenet.

    Will return :http:statuscode:`200` on success.

    """

    carenet.delete()
    return DONE


@transaction.commit_on_success
def carenet_rename(request, carenet):
    """ Change a carenet's name.

    request.POST must contain:
    
    * *name*: The new name for the carenet.
    
    Will return :http:statuscode:`200` with XML describing the renamed
    carenet on success, :http:statuscode:`400` if *name* wasn't passed
    or if a carenet named *name* already exists on this record.

    """

    if request.POST.has_key(NAME):
        try:
            carenet.name = request.POST[NAME]
            carenet.save()
        except IntegrityError:
            transaction.rollback()
            return HttpResponseBadRequest('Carenet name is already taken')                  # Indivo UI relies on this string to identify the reason of the 400 being returned
        return render_template('carenets', {'carenets': [carenet], 'record':carenet.record}, type="xml")
    return HttpResponseBadRequest('Please provide a new name for the carenet')
