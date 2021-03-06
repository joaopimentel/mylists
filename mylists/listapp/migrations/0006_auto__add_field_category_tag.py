# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Category.tag'
        db.add_column('listapp_category', 'tag',
                      self.gf('django.db.models.fields.SlugField')(default=datetime.datetime(2013, 1, 11, 0, 0), unique=True, max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Category.tag'
        db.delete_column('listapp_category', 'tag')


    models = {
        'listapp.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '63'}),
            'tag': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        'listapp.link': {
            'Meta': {'object_name': 'Link'},
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['listapp.Category']", 'symmetrical': 'False', 'blank': 'True'}),
            'comment': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '2000', 'null': 'True', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '2000'})
        }
    }

    complete_apps = ['listapp']