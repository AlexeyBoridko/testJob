# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserInfo'
        db.create_table(u'testTicketsApp_userinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='', max_length=50)),
            ('surname', self.gf('django.db.models.fields.CharField')(default='', max_length=50)),
            ('date_of_birth', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 10, 10, 0, 0))),
            ('bio', self.gf('django.db.models.fields.TextField')(default='')),
            ('email', self.gf('django.db.models.fields.CharField')(default='', max_length=50)),
            ('jid', self.gf('django.db.models.fields.CharField')(default='', max_length=50)),
            ('skype_id', self.gf('django.db.models.fields.CharField')(default='', max_length=50)),
            ('other_contacts', self.gf('django.db.models.fields.TextField')(default='')),
        ))
        db.send_create_signal(u'testTicketsApp', ['UserInfo'])


    def backwards(self, orm):
        # Deleting model 'UserInfo'
        db.delete_table(u'testTicketsApp_userinfo')


    models = {
        u'testTicketsApp.userinfo': {
            'Meta': {'object_name': 'UserInfo'},
            'bio': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'date_of_birth': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 10, 10, 0, 0)'}),
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