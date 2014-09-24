# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Client'
        db.create_table(u'core_client', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('domain_url', self.gf('django.db.models.fields.CharField')(unique=True, max_length=128)),
            ('schema_name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=63)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=180)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=180)),
            ('created_on', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Client'])


    def backwards(self, orm):
        # Deleting model 'Client'
        db.delete_table(u'core_client')


    models = {
        u'core.client': {
            'Meta': {'ordering': "['-created_on']", 'object_name': 'Client'},
            'created_on': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'domain_url': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '180'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '180'}),
            'schema_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '63'})
        }
    }

    complete_apps = ['core']