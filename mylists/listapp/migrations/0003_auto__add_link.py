# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Link'
        db.create_table('listapp_link', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('url', self.gf('django.db.models.fields.SlugField')(max_length=2000)),
            ('comment', self.gf('django.db.models.fields.CharField')(default='', max_length=2000, null=True, blank=True)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal('listapp', ['Link'])


    def backwards(self, orm):
        # Deleting model 'Link'
        db.delete_table('listapp_link')


    models = {
        'listapp.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '63'})
        },
        'listapp.link': {
            'Meta': {'object_name': 'Link'},
            'comment': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.SlugField', [], {'max_length': '2000'})
        }
    }

    complete_apps = ['listapp']