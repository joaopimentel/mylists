# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field category on 'Link'
        db.create_table('listapp_link_category', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('link', models.ForeignKey(orm['listapp.link'], null=False)),
            ('category', models.ForeignKey(orm['listapp.category'], null=False))
        ))
        db.create_unique('listapp_link_category', ['link_id', 'category_id'])


    def backwards(self, orm):
        # Removing M2M table for field category on 'Link'
        db.delete_table('listapp_link_category')


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
            'url': ('django.db.models.fields.SlugField', [], {'max_length': '2000'})
        }
    }

    complete_apps = ['listapp']