# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Principal'
        db.create_table('indivo_principal', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='principal_created_by', null=True, to=orm['indivo.Principal'])),
            ('email', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('indivo', ['Principal'])

        # Adding model 'NoUser'
        db.create_table('indivo_nouser', (
            ('principal_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['indivo.Principal'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('indivo', ['NoUser'])

        # Adding model 'Account'
        db.create_table('indivo_account', (
            ('account', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['indivo.Principal'], unique=True, primary_key=True)),
            ('primary_secret', self.gf('django.db.models.fields.CharField')(max_length=16, null=True)),
            ('secondary_secret', self.gf('django.db.models.fields.CharField')(max_length=8, null=True)),
            ('full_name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('contact_email', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('last_login_at', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('last_failed_login_at', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('total_login_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('failed_login_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('cancerDisease', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('placeOfResidence', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('sharingPreferences', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('role', self.gf('django.db.models.fields.CharField')(default='patient', max_length=50)),
            ('speciality', self.gf('django.db.models.fields.CharField')(max_length=350, null=True)),
            ('health_organisation', self.gf('django.db.models.fields.CharField')(max_length=350, null=True)),
            ('address_organisation', self.gf('django.db.models.fields.CharField')(max_length=350, null=True)),
            ('state', self.gf('django.db.models.fields.CharField')(default='uninitialized', max_length=50)),
            ('last_state_change', self.gf('django.db.models.fields.DateTimeField')(null=True)),
        ))
        db.send_create_signal('indivo', ['Account'])

        # Adding model 'AuthSystem'
        db.create_table('indivo_authsystem', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='authsystem_created_by', null=True, to=orm['indivo.Principal'])),
            ('short_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=100)),
            ('internal_p', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('indivo', ['AuthSystem'])

        # Adding model 'AccountAuthSystem'
        db.create_table('indivo_accountauthsystem', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='accountauthsystem_created_by', null=True, to=orm['indivo.Principal'])),
            ('account', self.gf('django.db.models.fields.related.ForeignKey')(related_name='auth_systems', to=orm['indivo.Account'])),
            ('auth_system', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indivo.AuthSystem'])),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('auth_parameters', self.gf('django.db.models.fields.CharField')(max_length=2000, null=True)),
            ('user_attributes', self.gf('django.db.models.fields.CharField')(max_length=2000, null=True)),
        ))
        db.send_create_signal('indivo', ['AccountAuthSystem'])

        # Adding unique constraint on 'AccountAuthSystem', fields ['auth_system', 'account']
        db.create_unique('indivo_accountauthsystem', ['auth_system_id', 'account_id'])

        # Adding unique constraint on 'AccountAuthSystem', fields ['auth_system', 'username']
        db.create_unique('indivo_accountauthsystem', ['auth_system_id', 'username'])

        # Adding model 'Carenet'
        db.create_table('indivo_carenet', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='carenet_created_by', null=True, to=orm['indivo.Principal'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('record', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indivo.Record'])),
        ))
        db.send_create_signal('indivo', ['Carenet'])

        # Adding unique constraint on 'Carenet', fields ['name', 'record']
        db.create_unique('indivo_carenet', ['name', 'record_id'])

        # Adding model 'CarenetDocument'
        db.create_table('indivo_carenetdocument', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='carenetdocument_created_by', null=True, to=orm['indivo.Principal'])),
            ('carenet', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indivo.Carenet'])),
            ('document', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indivo.Document'])),
            ('share_p', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('indivo', ['CarenetDocument'])

        # Adding unique constraint on 'CarenetDocument', fields ['carenet', 'document']
        db.create_unique('indivo_carenetdocument', ['carenet_id', 'document_id'])

        # Adding model 'CarenetPHA'
        db.create_table('indivo_carenetpha', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='carenetpha_created_by', null=True, to=orm['indivo.Principal'])),
            ('carenet', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indivo.Carenet'])),
            ('pha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indivo.PHA'])),
        ))
        db.send_create_signal('indivo', ['CarenetPHA'])

        # Adding unique constraint on 'CarenetPHA', fields ['carenet', 'pha']
        db.create_unique('indivo_carenetpha', ['carenet_id', 'pha_id'])

        # Adding model 'CarenetAccount'
        db.create_table('indivo_carenetaccount', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='carenetaccount_created_by', null=True, to=orm['indivo.Principal'])),
            ('carenet', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indivo.Carenet'])),
            ('account', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indivo.Account'])),
            ('can_write', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('indivo', ['CarenetAccount'])

        # Adding unique constraint on 'CarenetAccount', fields ['carenet', 'account']
        db.create_unique('indivo_carenetaccount', ['carenet_id', 'account_id'])

        # Adding model 'CarenetAutoshare'
        db.create_table('indivo_carenetautoshare', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='carenetautoshare_created_by', null=True, to=orm['indivo.Principal'])),
            ('carenet', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indivo.Carenet'])),
            ('record', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indivo.Record'])),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indivo.DocumentSchema'], null=True)),
        ))
        db.send_create_signal('indivo', ['CarenetAutoshare'])

        # Adding unique constraint on 'CarenetAutoshare', fields ['carenet', 'record', 'type']
        db.create_unique('indivo_carenetautoshare', ['carenet_id', 'record_id', 'type_id'])

        # Adding model 'AccountFullShare'
        db.create_table('indivo_accountfullshare', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='accountfullshare_created_by', null=True, to=orm['indivo.Principal'])),
            ('record', self.gf('django.db.models.fields.related.ForeignKey')(related_name='fullshares', to=orm['indivo.Record'])),
            ('with_account', self.gf('django.db.models.fields.related.ForeignKey')(related_name='fullshares_to', to=orm['indivo.Account'])),
            ('role_label', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
        ))
        db.send_create_signal('indivo', ['AccountFullShare'])

        # Adding unique constraint on 'AccountFullShare', fields ['record', 'with_account']
        db.create_unique('indivo_accountfullshare', ['record_id', 'with_account_id'])

        # Adding model 'PHAShare'
        db.create_table('indivo_phashare', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='phashare_created_by', null=True, to=orm['indivo.Principal'])),
            ('record', self.gf('django.db.models.fields.related.ForeignKey')(related_name='pha_shares', to=orm['indivo.Record'])),
            ('with_pha', self.gf('django.db.models.fields.related.ForeignKey')(related_name='pha_shares_to', to=orm['indivo.PHA'])),
            ('authorized_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('authorized_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='shares_authorized_by', null=True, to=orm['indivo.Account'])),
            ('carenet', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indivo.Carenet'], null=True)),
        ))
        db.send_create_signal('indivo', ['PHAShare'])

        # Adding unique constraint on 'PHAShare', fields ['record', 'with_pha']
        db.create_unique('indivo_phashare', ['record_id', 'with_pha_id'])

        # Adding model 'AccessToken'
        db.create_table('indivo_accesstoken', (
            ('principal_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['indivo.Principal'], unique=True, primary_key=True)),
            ('token', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('token_secret', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('share', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indivo.PHAShare'])),
            ('account', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indivo.Account'], null=True)),
            ('carenet', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indivo.Carenet'], null=True)),
            ('expires_at', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('connect_auth_p', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('indivo', ['AccessToken'])

        # Adding model 'ReqToken'
        db.create_table('indivo_reqtoken', (
            ('principal_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['indivo.Principal'], unique=True, primary_key=True)),
            ('token', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('token_secret', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('verifier', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('oauth_callback', self.gf('django.db.models.fields.CharField')(max_length=500, null=True)),
            ('pha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indivo.PHA'])),
            ('record', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indivo.Record'], null=True)),
            ('carenet', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indivo.Carenet'], null=True)),
            ('authorized_at', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('authorized_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indivo.Account'], null=True)),
            ('share', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indivo.PHAShare'], null=True)),
        ))
        db.send_create_signal('indivo', ['ReqToken'])

        # Adding model 'Message'
        db.create_table('indivo_message', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='message_created_by', null=True, to=orm['indivo.Principal'])),
            ('account', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indivo.Account'])),
            ('about_record', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indivo.Record'], null=True)),
            ('external_identifier', self.gf('django.db.models.fields.CharField')(max_length=250, null=True)),
            ('sender', self.gf('django.db.models.fields.related.ForeignKey')(related_name='message_as_sender', to=orm['indivo.Principal'])),
            ('recipient', self.gf('django.db.models.fields.related.ForeignKey')(related_name='message_as_recipient', to=orm['indivo.Principal'])),
            ('severity', self.gf('django.db.models.fields.CharField')(default='low', max_length=100)),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('body_type', self.gf('django.db.models.fields.CharField')(default='plaintext', max_length=100)),
            ('body', self.gf('django.db.models.fields.TextField')()),
            ('received_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('read_at', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('archived_at', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('response_to', self.gf('django.db.models.fields.related.ForeignKey')(related_name='message_responses', null=True, to=orm['indivo.Message'])),
            ('num_attachments', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('indivo', ['Message'])

        # Adding unique constraint on 'Message', fields ['account', 'external_identifier', 'sender']
        db.create_unique('indivo_message', ['account_id', 'external_identifier', 'sender_id'])

        # Adding model 'MessageAttachment'
        db.create_table('indivo_messageattachment', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='messageattachment_created_by', null=True, to=orm['indivo.Principal'])),
            ('message', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indivo.Message'])),
            ('size', self.gf('django.db.models.fields.IntegerField')()),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('content', self.gf('django.db.models.fields.TextField')()),
            ('saved_to_document', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indivo.Document'], null=True)),
            ('attachment_num', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('indivo', ['MessageAttachment'])

        # Adding unique constraint on 'MessageAttachment', fields ['message', 'attachment_num']
        db.create_unique('indivo_messageattachment', ['message_id', 'attachment_num'])

        # Adding model 'Notification'
        db.create_table('indivo_notification', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='notification_created_by', null=True, to=orm['indivo.Principal'])),
            ('account', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indivo.Account'])),
            ('record', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indivo.Record'], null=True)),
            ('sender', self.gf('django.db.models.fields.related.ForeignKey')(related_name='notifications_sent_by', to=orm['indivo.Principal'])),
            ('content', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('document', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indivo.Document'], null=True)),
            ('app_url', self.gf('django.db.models.fields.CharField')(max_length=300, null=True)),
        ))
        db.send_create_signal('indivo', ['Notification'])

        # Adding model 'RecordNotificationRoute'
        db.create_table('indivo_recordnotificationroute', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='recordnotificationroute_created_by', null=True, to=orm['indivo.Principal'])),
            ('record', self.gf('django.db.models.fields.related.ForeignKey')(related_name='notification_routes', to=orm['indivo.Record'])),
            ('account', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indivo.Account'])),
        ))
        db.send_create_signal('indivo', ['RecordNotificationRoute'])

        # Adding unique constraint on 'RecordNotificationRoute', fields ['account', 'record']
        db.create_unique('indivo_recordnotificationroute', ['account_id', 'record_id'])

        # Adding model 'StatusName'
        db.create_table('indivo_statusname', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=24)),
        ))
        db.send_create_signal('indivo', ['StatusName'])

        # Adding model 'DocumentStatusHistory'
        db.create_table('indivo_documentstatushistory', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='documentstatushistory_created_by', null=True, to=orm['indivo.Principal'])),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indivo.StatusName'])),
            ('reason', self.gf('django.db.models.fields.TextField')()),
            ('document', self.gf('django.db.models.fields.CharField')(max_length=64, null=True)),
            ('record', self.gf('django.db.models.fields.CharField')(max_length=64, null=True)),
            ('proxied_by_principal', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('effective_principal', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
        ))
        db.send_create_signal('indivo', ['DocumentStatusHistory'])

        # Adding model 'Record'
        db.create_table('indivo_record', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='record_created_by', null=True, to=orm['indivo.Principal'])),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='records_owned_by', null=True, to=orm['indivo.Principal'])),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=60, null=True)),
            ('external_id', self.gf('django.db.models.fields.CharField')(max_length=250, unique=True, null=True)),
            ('demographics', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['indivo.Demographics'], unique=True, null=True)),
        ))
        db.send_create_signal('indivo', ['Record'])

        # Adding model 'DocumentSchema'
        db.create_table('indivo_documentschema', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='documentschema_created_by', null=True, to=orm['indivo.Principal'])),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('stylesheet', self.gf('django.db.models.fields.related.ForeignKey')(related_name='stylesheet', null=True, to=orm['indivo.Document'])),
            ('internal_p', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('indivo', ['DocumentSchema'])

        # Adding model 'Document'
        db.create_table('indivo_document', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='document_created_by', null=True, to=orm['indivo.Principal'])),
            ('record', self.gf('django.db.models.fields.related.ForeignKey')(related_name='documents', null=True, to=orm['indivo.Record'])),
            ('external_id', self.gf('django.db.models.fields.CharField')(max_length=250, null=True)),
            ('nevershare', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('fqn', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('mime_type', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('content', self.gf('django.db.models.fields.TextField')(null=True)),
            ('content_file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('pha', self.gf('django.db.models.fields.related.ForeignKey')(related_name='pha_document', null=True, to=orm['indivo.PHA'])),
            ('suppressed_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('suppressed_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indivo.Principal'], null=True)),
            ('original', self.gf('django.db.models.fields.related.ForeignKey')(related_name='document_thread', null=True, to=orm['indivo.Document'])),
            ('replaced_by', self.gf('django.db.models.fields.related.ForeignKey')(related_name='document_replaced', null=True, to=orm['indivo.Document'])),
            ('replaces', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indivo.Document'], null=True)),
            ('size', self.gf('django.db.models.fields.IntegerField')()),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=100, null=True)),
            ('digest', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('status', self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['indivo.StatusName'])),
            ('processed', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('indivo', ['Document'])

        # Adding unique constraint on 'Document', fields ['record', 'external_id']
        db.create_unique('indivo_document', ['record_id', 'external_id'])

        # Adding model 'Nonce'
        db.create_table('indivo_nonce', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nonce', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('oauth_type', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('indivo', ['Nonce'])

        # Adding unique constraint on 'Nonce', fields ['nonce', 'oauth_type']
        db.create_unique('indivo_nonce', ['nonce', 'oauth_type'])

        # Adding model 'PHA'
        db.create_table('indivo_pha', (
            ('principal_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['indivo.Principal'], unique=True, primary_key=True)),
            ('consumer_key', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('secret', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=2000, null=True)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=40, null=True)),
            ('indivo_version', self.gf('django.db.models.fields.CharField')(max_length=40, null=True)),
            ('start_url_template', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('callback_url', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('is_autonomous', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('autonomous_reason', self.gf('django.db.models.fields.TextField')(null=True)),
            ('has_ui', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('frameable', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('icon_url', self.gf('django.db.models.fields.CharField')(max_length=500, null=True)),
            ('requirements', self.gf('django.db.models.fields.TextField')(null=True)),
        ))
        db.send_create_signal('indivo', ['PHA'])

        # Adding model 'MachineApp'
        db.create_table('indivo_machineapp', (
            ('principal_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['indivo.Principal'], unique=True, primary_key=True)),
            ('consumer_key', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('secret', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=2000, null=True)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=40, null=True)),
            ('indivo_version', self.gf('django.db.models.fields.CharField')(max_length=40, null=True)),
            ('app_type', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('indivo', ['MachineApp'])

        # Adding model 'SessionRequestToken'
        db.create_table('indivo_sessionrequesttoken', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sessionrequesttoken_created_by', null=True, to=orm['indivo.Principal'])),
            ('token', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('secret', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indivo.Account'], null=True)),
            ('approved_p', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('indivo', ['SessionRequestToken'])

        # Adding model 'SessionToken'
        db.create_table('indivo_sessiontoken', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='sessiontoken_created_by', null=True, to=orm['indivo.Principal'])),
            ('token', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('secret', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indivo.Account'], null=True)),
            ('expires_at', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('indivo', ['SessionToken'])

        # Adding model 'Demographics'
        db.create_table('indivo_demographics', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('document', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indivo.Document'], null=True, blank=True)),
            ('bday', self.gf('django.db.models.fields.DateField')(blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('ethnicity', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('preferred_language', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('race', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('siop', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('pregnancy', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('weight', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('weight_unit', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('smoking', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('adr_region', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('adr_country', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('adr_postalcode', self.gf('django.db.models.fields.CharField')(max_length=12, null=True, blank=True)),
            ('adr_city', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('adr_street', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('tel_2_type', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('tel_2_preferred_p', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tel_2_number', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('tel_1_type', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('tel_1_preferred_p', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tel_1_number', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('name_given', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('name_prefix', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('name_suffix', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('name_family', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('name_middle', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('indivo', ['Demographics'])

        # Adding model 'DocumentRels'
        db.create_table('indivo_documentrels', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('document_0', self.gf('django.db.models.fields.related.ForeignKey')(related_name='rels_as_doc_0', to=orm['indivo.Document'])),
            ('document_1', self.gf('django.db.models.fields.related.ForeignKey')(related_name='rels_as_doc_1', to=orm['indivo.Document'])),
            ('relationship', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indivo.DocumentSchema'])),
        ))
        db.send_create_signal('indivo', ['DocumentRels'])

        # Adding model 'Audit'
        db.create_table('indivo_audit', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('view_func', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('request_successful', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('effective_principal_email', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('proxied_by_email', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('carenet_id', self.gf('django.db.models.fields.CharField')(max_length=64, null=True)),
            ('record_id', self.gf('django.db.models.fields.CharField')(max_length=64, null=True)),
            ('pha_id', self.gf('django.db.models.fields.CharField')(max_length=64, null=True)),
            ('document_id', self.gf('django.db.models.fields.CharField')(max_length=64, null=True)),
            ('external_id', self.gf('django.db.models.fields.CharField')(max_length=250, null=True)),
            ('message_id', self.gf('django.db.models.fields.CharField')(max_length=250, null=True)),
            ('req_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True)),
            ('req_ip_address', self.gf('django.db.models.fields.IPAddressField')(max_length=15, null=True)),
            ('req_domain', self.gf('django.db.models.fields.URLField')(max_length=200, null=True)),
            ('req_headers', self.gf('django.db.models.fields.TextField')(null=True)),
            ('req_method', self.gf('django.db.models.fields.CharField')(max_length=12, null=True)),
            ('resp_code', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('resp_headers', self.gf('django.db.models.fields.TextField')(null=True)),
        ))
        db.send_create_signal('indivo', ['Audit'])

        # Adding model 'Fact'
        db.create_table('indivo_fact', (
            ('id', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('document', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indivo.Document'], null=True, blank=True)),
            ('record', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indivo.Record'], null=True, blank=True)),
        ))
        db.send_create_signal('indivo', ['Fact'])

        # Adding model 'SimpleClinicalNote'
        db.create_table('indivo_simpleclinicalnote', (
            ('fact_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['indivo.Fact'], unique=True, primary_key=True)),
            ('date_of_visit', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('finalized_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('visit_type', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('visit_type_type', self.gf('django.db.models.fields.CharField')(max_length=80, null=True, blank=True)),
            ('visit_type_value', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('visit_type_abbrev', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('visit_location', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('specialty', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('specialty_type', self.gf('django.db.models.fields.CharField')(max_length=80, null=True, blank=True)),
            ('specialty_value', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('specialty_abbrev', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('signed_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('provider_name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('provider_institution', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('chief_complaint', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('indivo', ['SimpleClinicalNote'])

        # Adding model 'VitalSigns'
        db.create_table('indivo_vitalsigns', (
            ('fact_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['indivo.Fact'], unique=True, primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('encounter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['indivo.Encounter'], null=True, blank=True)),
            ('temperature_unit', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('temperature_value', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('temperature_name_identifier', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('temperature_name_system', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('temperature_name_title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('weight_unit', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('weight_value', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('weight_name_identifier', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('weight_name_system', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('weight_name_title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('oxygen_saturation_unit', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('oxygen_saturation_value', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('oxygen_saturation_name_identifier', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('oxygen_saturation_name_system', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('oxygen_saturation_name_title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('bmi_unit', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('bmi_value', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('bmi_name_identifier', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('bmi_name_system', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('bmi_name_title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('respiratory_rate_unit', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('respiratory_rate_value', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('respiratory_rate_name_identifier', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('respiratory_rate_name_system', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('respiratory_rate_name_title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('height_unit', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('height_value', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('height_name_identifier', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('height_name_system', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('height_name_title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('heart_rate_unit', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('heart_rate_value', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('heart_rate_name_identifier', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('heart_rate_name_system', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('heart_rate_name_title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('bp_diastolic_unit', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('bp_diastolic_value', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('bp_diastolic_name_identifier', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('bp_diastolic_name_system', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('bp_diastolic_name_title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('bp_method_identifier', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('bp_method_system', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('bp_method_title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('bp_site_identifier', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('bp_site_system', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('bp_site_title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('bp_systolic_unit', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('bp_systolic_value', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('bp_systolic_name_identifier', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('bp_systolic_name_system', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('bp_systolic_name_title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('bp_position_identifier', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('bp_position_system', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('bp_position_title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('indivo', ['VitalSigns'])

        # Adding model 'Encounter'
        db.create_table('indivo_encounter', (
            ('fact_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['indivo.Fact'], unique=True, primary_key=True)),
            ('startDate', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('endDate', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('facility_adr_region', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('facility_adr_country', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('facility_adr_postalcode', self.gf('django.db.models.fields.CharField')(max_length=12, null=True, blank=True)),
            ('facility_adr_city', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('facility_adr_street', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('facility_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('encounterType_identifier', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('encounterType_system', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('encounterType_title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('provider_tel_1_type', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('provider_tel_1_preferred_p', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('provider_tel_1_number', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('provider_bday', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('provider_email', self.gf('django.db.models.fields.EmailField')(max_length=255, null=True, blank=True)),
            ('provider_npi_number', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('provider_adr_region', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('provider_adr_country', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('provider_adr_postalcode', self.gf('django.db.models.fields.CharField')(max_length=12, null=True, blank=True)),
            ('provider_adr_city', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('provider_adr_street', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('provider_gender', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('provider_tel_2_type', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('provider_tel_2_preferred_p', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('provider_tel_2_number', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('provider_race', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('provider_dea_number', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('provider_preferred_language', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('provider_ethnicity', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('provider_name_given', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('provider_name_prefix', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('provider_name_suffix', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('provider_name_family', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('provider_name_middle', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('indivo', ['Encounter'])

        # Adding model 'Measurements'
        db.create_table('indivo_measurements', (
            ('fact_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['indivo.Fact'], unique=True, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('name_value', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('name_abbrev', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('number', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('kind', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('unit', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('comments', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('measurementDate', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal('indivo', ['Measurements'])

        # Adding model 'edss'
        db.create_table('indivo_edss', (
            ('fact_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['indivo.Fact'], unique=True, primary_key=True)),
            ('date_performed', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('visual', self.gf('django.db.models.fields.CharField')(max_length=1000)),
            ('visualDe', self.gf('django.db.models.fields.CharField')(max_length=1000, blank=True)),
            ('brainstem', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True)),
            ('brainstemDe', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True)),
            ('pyramidal', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True)),
            ('pyramidalDe', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True)),
            ('cerebellar', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True)),
            ('cerebellarDe', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True)),
            ('sensory', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True)),
            ('sensoryDe', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True)),
            ('bladder', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True)),
            ('bladderDe', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True)),
            ('doctor_name', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True)),
            ('cerebral', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True)),
            ('cerebralDe', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True)),
            ('ambulation', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True)),
            ('ambulationDe', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True, blank=True)),
            ('score', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True)),
            ('comments', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('indivo', ['edss'])

        # Adding model 'Filedocument'
        db.create_table('indivo_filedocument', (
            ('fact_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['indivo.Fact'], unique=True, primary_key=True)),
            ('registered_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=800, null=True, blank=True)),
            ('file_id', self.gf('django.db.models.fields.CharField')(max_length=800, null=True, blank=True)),
            ('file_set_id', self.gf('django.db.models.fields.CharField')(max_length=800, null=True, blank=True)),
            ('type_of_file', self.gf('django.db.models.fields.CharField')(max_length=800, null=True, blank=True)),
            ('filename', self.gf('django.db.models.fields.CharField')(max_length=800)),
            ('file_base64', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('file', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('organisation', self.gf('django.db.models.fields.CharField')(max_length=800, null=True, blank=True)),
            ('doctor', self.gf('django.db.models.fields.CharField')(max_length=800, null=True, blank=True)),
            ('diagnosis', self.gf('django.db.models.fields.CharField')(max_length=800, null=True, blank=True)),
            ('reasons', self.gf('django.db.models.fields.CharField')(max_length=800, null=True, blank=True)),
            ('comments', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('indivo', ['Filedocument'])

        # Adding model 'Measurement'
        db.create_table('indivo_measurement', (
            ('fact_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['indivo.Fact'], unique=True, primary_key=True)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=24, blank=True)),
            ('value', self.gf('django.db.models.fields.FloatField')(blank=True)),
            ('unit', self.gf('django.db.models.fields.CharField')(max_length=8, blank=True)),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
        ))
        db.send_create_signal('indivo', ['Measurement'])

        # Adding model 'Appointment'
        db.create_table('indivo_appointment', (
            ('fact_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['indivo.Fact'], unique=True, primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('time', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('appointment_title', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('comments', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('lastname', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('street_number', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('route', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('locality', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('postal_code', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('alert', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
        ))
        db.send_create_signal('indivo', ['Appointment'])

        # Adding model 'Immunization'
        db.create_table('indivo_immunization', (
            ('fact_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['indivo.Fact'], unique=True, primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('product_class_identifier', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('product_class_system', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('product_class_title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('product_class_2_identifier', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('product_class_2_system', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('product_class_2_title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('refusal_reason_identifier', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('refusal_reason_system', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('refusal_reason_title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('administration_status_identifier', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('administration_status_system', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('administration_status_title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('product_name_identifier', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('product_name_system', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('product_name_title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
        ))
        db.send_create_signal('indivo', ['Immunization'])

        # Adding model 'Procedure'
        db.create_table('indivo_procedure', (
            ('fact_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['indivo.Fact'], unique=True, primary_key=True)),
            ('date_performed', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=800, null=True)),
            ('name_type', self.gf('django.db.models.fields.CharField')(max_length=800, blank=True)),
            ('name_value', self.gf('django.db.models.fields.CharField')(max_length=800, null=True, blank=True)),
            ('name_abbrev', self.gf('django.db.models.fields.CharField')(max_length=800, null=True, blank=True)),
            ('provider_name', self.gf('django.db.models.fields.CharField')(max_length=800, null=True, blank=True)),
            ('provider_institution', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('comments', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('indivo', ['Procedure'])

        # Adding model 'Seriousgames'
        db.create_table('indivo_seriousgames', (
            ('fact_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['indivo.Fact'], unique=True, primary_key=True)),
            ('createdAt', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('extraWeapons', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True)),
            ('registerCode', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('registerEnabled', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('supportEnabled', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('userId', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('registered', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal('indivo', ['Seriousgames'])

        # Adding model 'Allergy'
        db.create_table('indivo_allergy', (
            ('fact_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['indivo.Fact'], unique=True, primary_key=True)),
            ('category_identifier', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('category_system', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('category_title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('food_allergen_identifier', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('food_allergen_system', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('food_allergen_title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('severity_identifier', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('severity_system', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('severity_title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('drug_allergen_identifier', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('drug_allergen_system', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('drug_allergen_title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('drug_class_allergen_identifier', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('drug_class_allergen_system', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('drug_class_allergen_title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('allergic_reaction_identifier', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('allergic_reaction_system', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('allergic_reaction_title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
        ))
        db.send_create_signal('indivo', ['Allergy'])

        # Adding model 'AllergyExclusion'
        db.create_table('indivo_allergyexclusion', (
            ('fact_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['indivo.Fact'], unique=True, primary_key=True)),
            ('name_identifier', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('name_system', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('name_title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
        ))
        db.send_create_signal('indivo', ['AllergyExclusion'])

        # Adding model 'Equipment'
        db.create_table('indivo_equipment', (
            ('fact_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['indivo.Fact'], unique=True, primary_key=True)),
            ('date_started', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('date_stopped', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
            ('vendor', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal('indivo', ['Equipment'])

        # Adding model 'Problem'
        db.create_table('indivo_problem', (
            ('fact_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['indivo.Fact'], unique=True, primary_key=True)),
            ('startDate', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('endDate', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('category', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('name_identifier', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('name_system', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('name_title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
        ))
        db.send_create_signal('indivo', ['Problem'])

        # Adding model 'LabResult'
        db.create_table('indivo_labresult', (
            ('fact_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['indivo.Fact'], unique=True, primary_key=True)),
            ('accession_number', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('narrative_result', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('notes', self.gf('django.db.models.fields.CharField')(max_length=600, null=True, blank=True)),
            ('collected_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('collected_by_role', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('status_identifier', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('status_system', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('status_title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('quantitative_result_value_value', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('quantitative_result_value_unit', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('quantitative_result_non_critical_range_min_value', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('quantitative_result_non_critical_range_min_unit', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('quantitative_result_non_critical_range_max_value', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('quantitative_result_non_critical_range_max_unit', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('quantitative_result_normal_range_min_value', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('quantitative_result_normal_range_min_unit', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('quantitative_result_normal_range_max_value', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('quantitative_result_normal_range_max_unit', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('abnormal_interpretation_identifier', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('abnormal_interpretation_system', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('abnormal_interpretation_title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('collected_by_org_adr_region', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('collected_by_org_adr_country', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('collected_by_org_adr_postalcode', self.gf('django.db.models.fields.CharField')(max_length=12, null=True, blank=True)),
            ('collected_by_org_adr_city', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('collected_by_org_adr_street', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('collected_by_org_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('test_name_identifier', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('test_name_system', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('test_name_title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('collected_by_name_given', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('collected_by_name_prefix', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('collected_by_name_suffix', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('collected_by_name_family', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('collected_by_name_middle', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('indivo', ['LabResult'])

        # Adding model 'Auditlog'
        db.create_table('indivo_auditlog', (
            ('fact_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['indivo.Fact'], unique=True, primary_key=True)),
            ('app_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('app_module', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('event_name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('event_parameters', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('patient', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, null=True, blank=True)),
            ('flag', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('indivo', ['Auditlog'])

        # Adding model 'Medication'
        db.create_table('indivo_medication', (
            ('fact_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['indivo.Fact'], unique=True, primary_key=True)),
            ('endDate', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('instructions', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('startDate', self.gf('django.db.models.fields.DateField')(null=True)),
            ('drugNumber', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('ingredients', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('drugIntakes', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('addingDate', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('lastEditDate', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('deletingEditDate', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('deletingFeedback', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('provenance_identifier', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('provenance_system', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('provenance_title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('frequency_value', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('frequency_unit', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('drugName_identifier', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('drugName_system', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('drugName_title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('quantity_value', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('quantity_unit', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('indivo', ['Medication'])

        # Adding model 'Fill'
        db.create_table('indivo_fill', (
            ('fact_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['indivo.Fact'], unique=True, primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('dispenseDaysSupply', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('pbm', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('medication', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='fulfillments', null=True, to=orm['indivo.Medication'])),
            ('pharmacy_ncpdpid', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('pharmacy_adr_region', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('pharmacy_adr_country', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('pharmacy_adr_postalcode', self.gf('django.db.models.fields.CharField')(max_length=12, null=True, blank=True)),
            ('pharmacy_adr_city', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('pharmacy_adr_street', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('pharmacy_org', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('provider_tel_1_type', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('provider_tel_1_preferred_p', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('provider_tel_1_number', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('provider_bday', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('provider_email', self.gf('django.db.models.fields.EmailField')(max_length=255, null=True, blank=True)),
            ('provider_npi_number', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('provider_adr_region', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('provider_adr_country', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('provider_adr_postalcode', self.gf('django.db.models.fields.CharField')(max_length=12, null=True, blank=True)),
            ('provider_adr_city', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('provider_adr_street', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('provider_gender', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('provider_tel_2_type', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('provider_tel_2_preferred_p', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('provider_tel_2_number', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('provider_race', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('provider_dea_number', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('provider_preferred_language', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('provider_ethnicity', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('provider_name_given', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('provider_name_prefix', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('provider_name_suffix', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('provider_name_family', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('provider_name_middle', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('quantityDispensed_value', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('quantityDispensed_unit', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('indivo', ['Fill'])


    def backwards(self, orm):
        # Removing unique constraint on 'Nonce', fields ['nonce', 'oauth_type']
        db.delete_unique('indivo_nonce', ['nonce', 'oauth_type'])

        # Removing unique constraint on 'Document', fields ['record', 'external_id']
        db.delete_unique('indivo_document', ['record_id', 'external_id'])

        # Removing unique constraint on 'RecordNotificationRoute', fields ['account', 'record']
        db.delete_unique('indivo_recordnotificationroute', ['account_id', 'record_id'])

        # Removing unique constraint on 'MessageAttachment', fields ['message', 'attachment_num']
        db.delete_unique('indivo_messageattachment', ['message_id', 'attachment_num'])

        # Removing unique constraint on 'Message', fields ['account', 'external_identifier', 'sender']
        db.delete_unique('indivo_message', ['account_id', 'external_identifier', 'sender_id'])

        # Removing unique constraint on 'PHAShare', fields ['record', 'with_pha']
        db.delete_unique('indivo_phashare', ['record_id', 'with_pha_id'])

        # Removing unique constraint on 'AccountFullShare', fields ['record', 'with_account']
        db.delete_unique('indivo_accountfullshare', ['record_id', 'with_account_id'])

        # Removing unique constraint on 'CarenetAutoshare', fields ['carenet', 'record', 'type']
        db.delete_unique('indivo_carenetautoshare', ['carenet_id', 'record_id', 'type_id'])

        # Removing unique constraint on 'CarenetAccount', fields ['carenet', 'account']
        db.delete_unique('indivo_carenetaccount', ['carenet_id', 'account_id'])

        # Removing unique constraint on 'CarenetPHA', fields ['carenet', 'pha']
        db.delete_unique('indivo_carenetpha', ['carenet_id', 'pha_id'])

        # Removing unique constraint on 'CarenetDocument', fields ['carenet', 'document']
        db.delete_unique('indivo_carenetdocument', ['carenet_id', 'document_id'])

        # Removing unique constraint on 'Carenet', fields ['name', 'record']
        db.delete_unique('indivo_carenet', ['name', 'record_id'])

        # Removing unique constraint on 'AccountAuthSystem', fields ['auth_system', 'username']
        db.delete_unique('indivo_accountauthsystem', ['auth_system_id', 'username'])

        # Removing unique constraint on 'AccountAuthSystem', fields ['auth_system', 'account']
        db.delete_unique('indivo_accountauthsystem', ['auth_system_id', 'account_id'])

        # Deleting model 'Principal'
        db.delete_table('indivo_principal')

        # Deleting model 'NoUser'
        db.delete_table('indivo_nouser')

        # Deleting model 'Account'
        db.delete_table('indivo_account')

        # Deleting model 'AuthSystem'
        db.delete_table('indivo_authsystem')

        # Deleting model 'AccountAuthSystem'
        db.delete_table('indivo_accountauthsystem')

        # Deleting model 'Carenet'
        db.delete_table('indivo_carenet')

        # Deleting model 'CarenetDocument'
        db.delete_table('indivo_carenetdocument')

        # Deleting model 'CarenetPHA'
        db.delete_table('indivo_carenetpha')

        # Deleting model 'CarenetAccount'
        db.delete_table('indivo_carenetaccount')

        # Deleting model 'CarenetAutoshare'
        db.delete_table('indivo_carenetautoshare')

        # Deleting model 'AccountFullShare'
        db.delete_table('indivo_accountfullshare')

        # Deleting model 'PHAShare'
        db.delete_table('indivo_phashare')

        # Deleting model 'AccessToken'
        db.delete_table('indivo_accesstoken')

        # Deleting model 'ReqToken'
        db.delete_table('indivo_reqtoken')

        # Deleting model 'Message'
        db.delete_table('indivo_message')

        # Deleting model 'MessageAttachment'
        db.delete_table('indivo_messageattachment')

        # Deleting model 'Notification'
        db.delete_table('indivo_notification')

        # Deleting model 'RecordNotificationRoute'
        db.delete_table('indivo_recordnotificationroute')

        # Deleting model 'StatusName'
        db.delete_table('indivo_statusname')

        # Deleting model 'DocumentStatusHistory'
        db.delete_table('indivo_documentstatushistory')

        # Deleting model 'Record'
        db.delete_table('indivo_record')

        # Deleting model 'DocumentSchema'
        db.delete_table('indivo_documentschema')

        # Deleting model 'Document'
        db.delete_table('indivo_document')

        # Deleting model 'Nonce'
        db.delete_table('indivo_nonce')

        # Deleting model 'PHA'
        db.delete_table('indivo_pha')

        # Deleting model 'MachineApp'
        db.delete_table('indivo_machineapp')

        # Deleting model 'SessionRequestToken'
        db.delete_table('indivo_sessionrequesttoken')

        # Deleting model 'SessionToken'
        db.delete_table('indivo_sessiontoken')

        # Deleting model 'Demographics'
        db.delete_table('indivo_demographics')

        # Deleting model 'DocumentRels'
        db.delete_table('indivo_documentrels')

        # Deleting model 'Audit'
        db.delete_table('indivo_audit')

        # Deleting model 'Fact'
        db.delete_table('indivo_fact')

        # Deleting model 'SimpleClinicalNote'
        db.delete_table('indivo_simpleclinicalnote')

        # Deleting model 'VitalSigns'
        db.delete_table('indivo_vitalsigns')

        # Deleting model 'Encounter'
        db.delete_table('indivo_encounter')

        # Deleting model 'Measurements'
        db.delete_table('indivo_measurements')

        # Deleting model 'edss'
        db.delete_table('indivo_edss')

        # Deleting model 'Filedocument'
        db.delete_table('indivo_filedocument')

        # Deleting model 'Measurement'
        db.delete_table('indivo_measurement')

        # Deleting model 'Appointment'
        db.delete_table('indivo_appointment')

        # Deleting model 'Immunization'
        db.delete_table('indivo_immunization')

        # Deleting model 'Procedure'
        db.delete_table('indivo_procedure')

        # Deleting model 'Seriousgames'
        db.delete_table('indivo_seriousgames')

        # Deleting model 'Allergy'
        db.delete_table('indivo_allergy')

        # Deleting model 'AllergyExclusion'
        db.delete_table('indivo_allergyexclusion')

        # Deleting model 'Equipment'
        db.delete_table('indivo_equipment')

        # Deleting model 'Problem'
        db.delete_table('indivo_problem')

        # Deleting model 'LabResult'
        db.delete_table('indivo_labresult')

        # Deleting model 'Auditlog'
        db.delete_table('indivo_auditlog')

        # Deleting model 'Medication'
        db.delete_table('indivo_medication')

        # Deleting model 'Fill'
        db.delete_table('indivo_fill')


    models = {
        'indivo.accesstoken': {
            'Meta': {'object_name': 'AccessToken', '_ormbases': ['indivo.Principal']},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Account']", 'null': 'True'}),
            'carenet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Carenet']", 'null': 'True'}),
            'connect_auth_p': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'expires_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'principal_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Principal']", 'unique': 'True', 'primary_key': 'True'}),
            'share': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.PHAShare']"}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'token_secret': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'indivo.account': {
            'Meta': {'object_name': 'Account', '_ormbases': ['indivo.Principal']},
            'account': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Principal']", 'unique': 'True', 'primary_key': 'True'}),
            'address_organisation': ('django.db.models.fields.CharField', [], {'max_length': '350', 'null': 'True'}),
            'cancerDisease': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'contact_email': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'failed_login_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'health_organisation': ('django.db.models.fields.CharField', [], {'max_length': '350', 'null': 'True'}),
            'last_failed_login_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'last_login_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'last_state_change': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'placeOfResidence': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'primary_secret': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True'}),
            'role': ('django.db.models.fields.CharField', [], {'default': "'patient'", 'max_length': '50'}),
            'secondary_secret': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True'}),
            'sharingPreferences': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'speciality': ('django.db.models.fields.CharField', [], {'max_length': '350', 'null': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'default': "'uninitialized'", 'max_length': '50'}),
            'total_login_count': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'indivo.accountauthsystem': {
            'Meta': {'unique_together': "(('auth_system', 'account'), ('auth_system', 'username'))", 'object_name': 'AccountAuthSystem'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'auth_systems'", 'to': "orm['indivo.Account']"}),
            'auth_parameters': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True'}),
            'auth_system': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.AuthSystem']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'accountauthsystem_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'user_attributes': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'indivo.accountfullshare': {
            'Meta': {'unique_together': "(('record', 'with_account'),)", 'object_name': 'AccountFullShare'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'accountfullshare_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fullshares'", 'to': "orm['indivo.Record']"}),
            'role_label': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'with_account': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fullshares_to'", 'to': "orm['indivo.Account']"})
        },
        'indivo.allergy': {
            'Meta': {'object_name': 'Allergy', '_ormbases': ['indivo.Fact']},
            'allergic_reaction_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'allergic_reaction_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'allergic_reaction_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'category_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'category_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'category_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'drug_allergen_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'drug_allergen_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'drug_allergen_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'drug_class_allergen_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'drug_class_allergen_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'drug_class_allergen_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'food_allergen_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'food_allergen_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'food_allergen_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'severity_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'severity_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'severity_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        },
        'indivo.allergyexclusion': {
            'Meta': {'object_name': 'AllergyExclusion', '_ormbases': ['indivo.Fact']},
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'name_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        },
        'indivo.appointment': {
            'Meta': {'object_name': 'Appointment', '_ormbases': ['indivo.Fact']},
            'alert': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'appointment_title': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'locality': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'route': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'street_number': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'time': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'indivo.audit': {
            'Meta': {'object_name': 'Audit'},
            'carenet_id': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'document_id': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'}),
            'effective_principal_email': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'external_id': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message_id': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'pha_id': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'}),
            'proxied_by_email': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'record_id': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'}),
            'req_domain': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'req_headers': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'req_ip_address': ('django.db.models.fields.IPAddressField', [], {'max_length': '15', 'null': 'True'}),
            'req_method': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True'}),
            'req_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'request_successful': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'resp_code': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'resp_headers': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'view_func': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        },
        'indivo.auditlog': {
            'Meta': {'object_name': 'Auditlog', '_ormbases': ['indivo.Fact']},
            'app_module': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'app_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'event_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'event_parameters': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'flag': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'patient': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'})
        },
        'indivo.authsystem': {
            'Meta': {'object_name': 'AuthSystem'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'authsystem_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'internal_p': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'short_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'})
        },
        'indivo.carenet': {
            'Meta': {'unique_together': "(('name', 'record'),)", 'object_name': 'Carenet'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'carenet_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Record']"})
        },
        'indivo.carenetaccount': {
            'Meta': {'unique_together': "(('carenet', 'account'),)", 'object_name': 'CarenetAccount'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Account']"}),
            'can_write': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'carenet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Carenet']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'carenetaccount_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'})
        },
        'indivo.carenetautoshare': {
            'Meta': {'unique_together': "(('carenet', 'record', 'type'),)", 'object_name': 'CarenetAutoshare'},
            'carenet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Carenet']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'carenetautoshare_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Record']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.DocumentSchema']", 'null': 'True'})
        },
        'indivo.carenetdocument': {
            'Meta': {'unique_together': "(('carenet', 'document'),)", 'object_name': 'CarenetDocument'},
            'carenet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Carenet']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'carenetdocument_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'document': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Document']"}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'share_p': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        'indivo.carenetpha': {
            'Meta': {'unique_together': "(('carenet', 'pha'),)", 'object_name': 'CarenetPHA'},
            'carenet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Carenet']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'carenetpha_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'pha': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.PHA']"})
        },
        'indivo.demographics': {
            'Meta': {'object_name': 'Demographics'},
            'adr_city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'adr_country': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'adr_postalcode': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'adr_region': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'adr_street': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bday': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'document': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Document']", 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'ethnicity': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name_family': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_given': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_middle': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_prefix': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_suffix': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'preferred_language': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'pregnancy': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'race': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'siop': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'smoking': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'tel_1_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'tel_1_preferred_p': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tel_1_type': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'tel_2_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'tel_2_preferred_p': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tel_2_type': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'weight_unit': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        'indivo.document': {
            'Meta': {'unique_together': "(('record', 'external_id'),)", 'object_name': 'Document'},
            'content': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'content_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'document_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'digest': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'external_id': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'fqn': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'mime_type': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'nevershare': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'original': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'document_thread'", 'null': 'True', 'to': "orm['indivo.Document']"}),
            'pha': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pha_document'", 'null': 'True', 'to': "orm['indivo.PHA']"}),
            'processed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'documents'", 'null': 'True', 'to': "orm['indivo.Record']"}),
            'replaced_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'document_replaced'", 'null': 'True', 'to': "orm['indivo.Document']"}),
            'replaces': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Document']", 'null': 'True'}),
            'size': ('django.db.models.fields.IntegerField', [], {}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': "orm['indivo.StatusName']"}),
            'suppressed_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'suppressed_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Principal']", 'null': 'True'})
        },
        'indivo.documentrels': {
            'Meta': {'object_name': 'DocumentRels'},
            'document_0': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rels_as_doc_0'", 'to': "orm['indivo.Document']"}),
            'document_1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rels_as_doc_1'", 'to': "orm['indivo.Document']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'relationship': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.DocumentSchema']"})
        },
        'indivo.documentschema': {
            'Meta': {'object_name': 'DocumentSchema'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'documentschema_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'internal_p': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'stylesheet': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'stylesheet'", 'null': 'True', 'to': "orm['indivo.Document']"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        'indivo.documentstatushistory': {
            'Meta': {'object_name': 'DocumentStatusHistory'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'documentstatushistory_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'document': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'}),
            'effective_principal': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'proxied_by_principal': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'reason': ('django.db.models.fields.TextField', [], {}),
            'record': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True'}),
            'status': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.StatusName']"})
        },
        'indivo.edss': {
            'Meta': {'object_name': 'edss', '_ormbases': ['indivo.Fact']},
            'ambulation': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'}),
            'ambulationDe': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'bladder': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'}),
            'bladderDe': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'brainstem': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'}),
            'brainstemDe': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'cerebellar': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'}),
            'cerebellarDe': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'cerebral': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'}),
            'cerebralDe': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date_performed': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'doctor_name': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'pyramidal': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'}),
            'pyramidalDe': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'score': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'}),
            'sensory': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True'}),
            'sensoryDe': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'visual': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'visualDe': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'blank': 'True'})
        },
        'indivo.encounter': {
            'Meta': {'object_name': 'Encounter', '_ormbases': ['indivo.Fact']},
            'encounterType_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'encounterType_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'encounterType_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'endDate': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'facility_adr_city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'facility_adr_country': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'facility_adr_postalcode': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'facility_adr_region': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'facility_adr_street': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'facility_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'provider_adr_city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_adr_country': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_adr_postalcode': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'provider_adr_region': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_adr_street': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_bday': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'provider_dea_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_email': ('django.db.models.fields.EmailField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_ethnicity': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_gender': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_name_family': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_name_given': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_name_middle': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_name_prefix': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_name_suffix': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_npi_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_preferred_language': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_race': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_tel_1_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'provider_tel_1_preferred_p': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'provider_tel_1_type': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'provider_tel_2_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'provider_tel_2_preferred_p': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'provider_tel_2_type': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'startDate': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        },
        'indivo.equipment': {
            'Meta': {'object_name': 'Equipment', '_ormbases': ['indivo.Fact']},
            'date_started': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_stopped': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'vendor': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'})
        },
        'indivo.fact': {
            'Meta': {'object_name': 'Fact'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'document': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Document']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Record']", 'null': 'True', 'blank': 'True'})
        },
        'indivo.filedocument': {
            'Meta': {'object_name': 'Filedocument', '_ormbases': ['indivo.Fact']},
            'comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'diagnosis': ('django.db.models.fields.CharField', [], {'max_length': '800', 'null': 'True', 'blank': 'True'}),
            'doctor': ('django.db.models.fields.CharField', [], {'max_length': '800', 'null': 'True', 'blank': 'True'}),
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'file_base64': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'file_id': ('django.db.models.fields.CharField', [], {'max_length': '800', 'null': 'True', 'blank': 'True'}),
            'file_set_id': ('django.db.models.fields.CharField', [], {'max_length': '800', 'null': 'True', 'blank': 'True'}),
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '800'}),
            'organisation': ('django.db.models.fields.CharField', [], {'max_length': '800', 'null': 'True', 'blank': 'True'}),
            'reasons': ('django.db.models.fields.CharField', [], {'max_length': '800', 'null': 'True', 'blank': 'True'}),
            'registered_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '800', 'null': 'True', 'blank': 'True'}),
            'type_of_file': ('django.db.models.fields.CharField', [], {'max_length': '800', 'null': 'True', 'blank': 'True'})
        },
        'indivo.fill': {
            'Meta': {'object_name': 'Fill', '_ormbases': ['indivo.Fact']},
            'date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'dispenseDaysSupply': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'medication': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'fulfillments'", 'null': 'True', 'to': "orm['indivo.Medication']"}),
            'pbm': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'pharmacy_adr_city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'pharmacy_adr_country': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'pharmacy_adr_postalcode': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'pharmacy_adr_region': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'pharmacy_adr_street': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'pharmacy_ncpdpid': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'pharmacy_org': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_adr_city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_adr_country': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_adr_postalcode': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'provider_adr_region': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_adr_street': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_bday': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'provider_dea_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_email': ('django.db.models.fields.EmailField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_ethnicity': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_gender': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_name_family': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_name_given': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_name_middle': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_name_prefix': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_name_suffix': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_npi_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_preferred_language': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_race': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provider_tel_1_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'provider_tel_1_preferred_p': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'provider_tel_1_type': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'provider_tel_2_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'provider_tel_2_preferred_p': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'provider_tel_2_type': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'quantityDispensed_unit': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'quantityDispensed_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'indivo.immunization': {
            'Meta': {'object_name': 'Immunization', '_ormbases': ['indivo.Fact']},
            'administration_status_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'administration_status_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'administration_status_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'product_class_2_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'product_class_2_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'product_class_2_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'product_class_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'product_class_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'product_class_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'product_name_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'product_name_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'product_name_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'refusal_reason_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'refusal_reason_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'refusal_reason_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'indivo.labresult': {
            'Meta': {'object_name': 'LabResult', '_ormbases': ['indivo.Fact']},
            'abnormal_interpretation_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'abnormal_interpretation_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'abnormal_interpretation_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'accession_number': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'collected_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'collected_by_name_family': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'collected_by_name_given': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'collected_by_name_middle': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'collected_by_name_prefix': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'collected_by_name_suffix': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'collected_by_org_adr_city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'collected_by_org_adr_country': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'collected_by_org_adr_postalcode': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'collected_by_org_adr_region': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'collected_by_org_adr_street': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'collected_by_org_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'collected_by_role': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'narrative_result': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '600', 'null': 'True', 'blank': 'True'}),
            'quantitative_result_non_critical_range_max_unit': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'quantitative_result_non_critical_range_max_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'quantitative_result_non_critical_range_min_unit': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'quantitative_result_non_critical_range_min_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'quantitative_result_normal_range_max_unit': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'quantitative_result_normal_range_max_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'quantitative_result_normal_range_min_unit': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'quantitative_result_normal_range_min_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'quantitative_result_value_unit': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'quantitative_result_value_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'status_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'status_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'status_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'test_name_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'test_name_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'test_name_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        },
        'indivo.machineapp': {
            'Meta': {'object_name': 'MachineApp'},
            'app_type': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'consumer_key': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True'}),
            'indivo_version': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'principal_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Principal']", 'unique': 'True', 'primary_key': 'True'}),
            'secret': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'})
        },
        'indivo.measurement': {
            'Meta': {'object_name': 'Measurement', '_ormbases': ['indivo.Fact']},
            'datetime': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '24', 'blank': 'True'}),
            'unit': ('django.db.models.fields.CharField', [], {'max_length': '8', 'blank': 'True'}),
            'value': ('django.db.models.fields.FloatField', [], {'blank': 'True'})
        },
        'indivo.measurements': {
            'Meta': {'object_name': 'Measurements', '_ormbases': ['indivo.Fact']},
            'comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'kind': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'measurementDate': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name_value': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'number': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'unit': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'})
        },
        'indivo.medication': {
            'Meta': {'object_name': 'Medication', '_ormbases': ['indivo.Fact']},
            'addingDate': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'deletingEditDate': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'deletingFeedback': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'drugIntakes': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'drugName_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'drugName_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'drugName_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'drugNumber': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'endDate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'frequency_unit': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'frequency_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'ingredients': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'instructions': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'lastEditDate': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'provenance_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provenance_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'provenance_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'quantity_unit': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'quantity_value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'startDate': ('django.db.models.fields.DateField', [], {'null': 'True'})
        },
        'indivo.message': {
            'Meta': {'unique_together': "(('account', 'external_identifier', 'sender'),)", 'object_name': 'Message'},
            'about_record': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Record']", 'null': 'True'}),
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Account']"}),
            'archived_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'body': ('django.db.models.fields.TextField', [], {}),
            'body_type': ('django.db.models.fields.CharField', [], {'default': "'plaintext'", 'max_length': '100'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'message_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'external_identifier': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'num_attachments': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'read_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'received_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'recipient': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'message_as_recipient'", 'to': "orm['indivo.Principal']"}),
            'response_to': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'message_responses'", 'null': 'True', 'to': "orm['indivo.Message']"}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'message_as_sender'", 'to': "orm['indivo.Principal']"}),
            'severity': ('django.db.models.fields.CharField', [], {'default': "'low'", 'max_length': '100'}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'indivo.messageattachment': {
            'Meta': {'unique_together': "(('message', 'attachment_num'),)", 'object_name': 'MessageAttachment'},
            'attachment_num': ('django.db.models.fields.IntegerField', [], {}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'messageattachment_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'message': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Message']"}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'saved_to_document': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Document']", 'null': 'True'}),
            'size': ('django.db.models.fields.IntegerField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        },
        'indivo.nonce': {
            'Meta': {'unique_together': "(('nonce', 'oauth_type'),)", 'object_name': 'Nonce'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nonce': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'oauth_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'})
        },
        'indivo.notification': {
            'Meta': {'object_name': 'Notification'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Account']"}),
            'app_url': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True'}),
            'content': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'notification_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'document': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Document']", 'null': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Record']", 'null': 'True'}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'notifications_sent_by'", 'to': "orm['indivo.Principal']"})
        },
        'indivo.nouser': {
            'Meta': {'object_name': 'NoUser', '_ormbases': ['indivo.Principal']},
            'principal_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Principal']", 'unique': 'True', 'primary_key': 'True'})
        },
        'indivo.pha': {
            'Meta': {'object_name': 'PHA'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'autonomous_reason': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'callback_url': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'consumer_key': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '2000', 'null': 'True'}),
            'frameable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'has_ui': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'icon_url': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'}),
            'indivo_version': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'}),
            'is_autonomous': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'principal_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Principal']", 'unique': 'True', 'primary_key': 'True'}),
            'requirements': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'secret': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'start_url_template': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True'})
        },
        'indivo.phashare': {
            'Meta': {'unique_together': "(('record', 'with_pha'),)", 'object_name': 'PHAShare'},
            'authorized_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'authorized_by': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'shares_authorized_by'", 'null': 'True', 'to': "orm['indivo.Account']"}),
            'carenet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Carenet']", 'null': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'phashare_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pha_shares'", 'to': "orm['indivo.Record']"}),
            'with_pha': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'pha_shares_to'", 'to': "orm['indivo.PHA']"})
        },
        'indivo.principal': {
            'Meta': {'object_name': 'Principal'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'principal_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'email': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'indivo.problem': {
            'Meta': {'object_name': 'Problem', '_ormbases': ['indivo.Fact']},
            'category': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'endDate': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'name_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'name_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'startDate': ('django.db.models.fields.DateTimeField', [], {'null': 'True'})
        },
        'indivo.procedure': {
            'Meta': {'object_name': 'Procedure', '_ormbases': ['indivo.Fact']},
            'comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date_performed': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '800', 'null': 'True'}),
            'name_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '800', 'null': 'True', 'blank': 'True'}),
            'name_type': ('django.db.models.fields.CharField', [], {'max_length': '800', 'blank': 'True'}),
            'name_value': ('django.db.models.fields.CharField', [], {'max_length': '800', 'null': 'True', 'blank': 'True'}),
            'provider_institution': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'provider_name': ('django.db.models.fields.CharField', [], {'max_length': '800', 'null': 'True', 'blank': 'True'})
        },
        'indivo.record': {
            'Meta': {'object_name': 'Record'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'record_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'demographics': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Demographics']", 'unique': 'True', 'null': 'True'}),
            'external_id': ('django.db.models.fields.CharField', [], {'max_length': '250', 'unique': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'records_owned_by'", 'null': 'True', 'to': "orm['indivo.Principal']"})
        },
        'indivo.recordnotificationroute': {
            'Meta': {'unique_together': "(('account', 'record'),)", 'object_name': 'RecordNotificationRoute'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Account']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'recordnotificationroute_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'notification_routes'", 'to': "orm['indivo.Record']"})
        },
        'indivo.reqtoken': {
            'Meta': {'object_name': 'ReqToken', '_ormbases': ['indivo.Principal']},
            'authorized_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'authorized_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Account']", 'null': 'True'}),
            'carenet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Carenet']", 'null': 'True'}),
            'oauth_callback': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'}),
            'pha': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.PHA']"}),
            'principal_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Principal']", 'unique': 'True', 'primary_key': 'True'}),
            'record': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Record']", 'null': 'True'}),
            'share': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.PHAShare']", 'null': 'True'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'token_secret': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'verifier': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'indivo.seriousgames': {
            'Meta': {'object_name': 'Seriousgames', '_ormbases': ['indivo.Fact']},
            'createdAt': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'extraWeapons': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'registerCode': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'registerEnabled': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'registered': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'supportEnabled': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'userId': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'indivo.sessionrequesttoken': {
            'Meta': {'object_name': 'SessionRequestToken'},
            'approved_p': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sessionrequesttoken_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'secret': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Account']", 'null': 'True'})
        },
        'indivo.sessiontoken': {
            'Meta': {'object_name': 'SessionToken'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sessiontoken_created_by'", 'null': 'True', 'to': "orm['indivo.Principal']"}),
            'expires_at': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'secret': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Account']", 'null': 'True'})
        },
        'indivo.simpleclinicalnote': {
            'Meta': {'object_name': 'SimpleClinicalNote', '_ormbases': ['indivo.Fact']},
            'chief_complaint': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date_of_visit': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'finalized_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'provider_institution': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'provider_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'signed_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'specialty': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'specialty_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'specialty_type': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'specialty_value': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'visit_location': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'visit_type': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'visit_type_abbrev': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'visit_type_type': ('django.db.models.fields.CharField', [], {'max_length': '80', 'null': 'True', 'blank': 'True'}),
            'visit_type_value': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'})
        },
        'indivo.statusname': {
            'Meta': {'object_name': 'StatusName'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '24'})
        },
        'indivo.vitalsigns': {
            'Meta': {'object_name': 'VitalSigns', '_ormbases': ['indivo.Fact']},
            'bmi_name_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bmi_name_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bmi_name_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bmi_unit': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bmi_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'bp_diastolic_name_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bp_diastolic_name_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bp_diastolic_name_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bp_diastolic_unit': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bp_diastolic_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'bp_method_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bp_method_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bp_method_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bp_position_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bp_position_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bp_position_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bp_site_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bp_site_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bp_site_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bp_systolic_name_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bp_systolic_name_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bp_systolic_name_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bp_systolic_unit': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'bp_systolic_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'encounter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['indivo.Encounter']", 'null': 'True', 'blank': 'True'}),
            'fact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['indivo.Fact']", 'unique': 'True', 'primary_key': 'True'}),
            'heart_rate_name_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'heart_rate_name_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'heart_rate_name_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'heart_rate_unit': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'heart_rate_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'height_name_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'height_name_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'height_name_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'height_unit': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'height_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'oxygen_saturation_name_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'oxygen_saturation_name_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'oxygen_saturation_name_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'oxygen_saturation_unit': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'oxygen_saturation_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'respiratory_rate_name_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'respiratory_rate_name_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'respiratory_rate_name_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'respiratory_rate_unit': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'respiratory_rate_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'temperature_name_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'temperature_name_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'temperature_name_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'temperature_unit': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'temperature_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'weight_name_identifier': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'weight_name_system': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'weight_name_title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'weight_unit': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'weight_value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['indivo']