# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MiddlewareRequests'
        db.create_table(u'testTicketsApp_middlewarerequests', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('request', self.gf('django.db.models.fields.CharField')(default='', max_length=255)),
            ('runtime', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'testTicketsApp', ['MiddlewareRequests'])


    def backwards(self, orm):
        # Deleting model 'MiddlewareRequests'
        db.delete_table(u'testTicketsApp_middlewarerequests')


    models = {
        u'testTicketsApp.middlewarerequests': {
            'Meta': {'object_name': 'MiddlewareRequests'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'request': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
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