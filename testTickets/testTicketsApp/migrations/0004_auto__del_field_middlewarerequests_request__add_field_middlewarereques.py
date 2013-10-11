# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'MiddlewareRequests.request'
        db.delete_column(u'testTicketsApp_middlewarerequests', 'request')

        # Adding field 'MiddlewareRequests.host'
        db.add_column(u'testTicketsApp_middlewarerequests', 'host',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'MiddlewareRequests.path'
        db.add_column(u'testTicketsApp_middlewarerequests', 'path',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Adding field 'MiddlewareRequests.method'
        db.add_column(u'testTicketsApp_middlewarerequests', 'method',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=20),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'MiddlewareRequests.request'
        db.add_column(u'testTicketsApp_middlewarerequests', 'request',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Deleting field 'MiddlewareRequests.host'
        db.delete_column(u'testTicketsApp_middlewarerequests', 'host')

        # Deleting field 'MiddlewareRequests.path'
        db.delete_column(u'testTicketsApp_middlewarerequests', 'path')

        # Deleting field 'MiddlewareRequests.method'
        db.delete_column(u'testTicketsApp_middlewarerequests', 'method')


    models = {
        u'testTicketsApp.middlewarerequests': {
            'Meta': {'object_name': 'MiddlewareRequests'},
            'host': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20'}),
            'path': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'runtime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'testTicketsApp.userinfo': {
            'Meta': {'object_name': 'UserInfo'},
            'bio': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'contacts': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'date_of_birth': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 10, 12, 0, 0)'}),
            'email': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jid': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'other_contacts': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'skype_id': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'surname': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'})
        }
    }

    complete_apps = ['testTicketsApp']