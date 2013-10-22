# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'MiddlewareRequests.priority'
        db.add_column(u'testTicketsApp_middlewarerequests', 'priority',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'MiddlewareRequests.priority'
        db.delete_column(u'testTicketsApp_middlewarerequests', 'priority')


    models = {
        u'testTicketsApp.middlewarerequests': {
            'Meta': {'object_name': 'MiddlewareRequests'},
            'host': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '20'}),
            'path': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'priority': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'runtime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'testTicketsApp.modelchangeslog': {
            'Meta': {'ordering': "['-runtime']", 'object_name': 'ModelChangesLog'},
            'action_type': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'runtime': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'testTicketsApp.userinfo': {
            'Meta': {'object_name': 'UserInfo'},
            'bio': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'contacts': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'date_of_birth': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 10, 23, 0, 0)'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '50', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jid': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'other_contacts': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'skype_id': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'surname': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'})
        }
    }

    complete_apps = ['testTicketsApp']