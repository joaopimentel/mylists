# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Link.url'
        db.alter_column('listapp_link', 'url', self.gf('django.db.models.fields.CharField')(max_length=2000))
        # Removing index on 'Link', fields ['url']
        db.delete_index('listapp_link', ['url'])


    def backwards(self, orm):
        # Adding index on 'Link', fields ['url']
        db.create_index('listapp_link', ['url'])


        # Changing field 'Link.url'
        db.alter_column('listapp_link', 'url', self.gf('django.db.models.fields.SlugField')(max_length=2000))

    models = {
        'listapp.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '63'})
        },
        'listapp.link': {
            'Meta': {'object_name': 'Link'},
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['listapp.Category']", 'symmetrical': 'False'}),
            'comment': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '2000'})
        }
    }

    complete_apps = ['listapp']