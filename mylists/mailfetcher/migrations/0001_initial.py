# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MailBox'
        db.create_table('mailfetcher_mailbox', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('mailfetcher', ['MailBox'])


    def backwards(self, orm):
        # Deleting model 'MailBox'
        db.delete_table('mailfetcher_mailbox')


    models = {
        'mailfetcher.mailbox': {
            'Meta': {'object_name': 'MailBox'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['mailfetcher']