# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Photo'
        db.create_table(u'photosong_photo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'photosong', ['Photo'])

        # Adding model 'Songs'
        db.create_table(u'photosong_songs', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('stream_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('download_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('artwork_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('waveform_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('genre', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('tag_list', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'photosong', ['Songs'])


    def backwards(self, orm):
        # Deleting model 'Photo'
        db.delete_table(u'photosong_photo')

        # Deleting model 'Songs'
        db.delete_table(u'photosong_songs')


    models = {
        u'photosong.photo': {
            'Meta': {'object_name': 'Photo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'photosong.songs': {
            'Meta': {'object_name': 'Songs'},
            'artwork_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'download_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'genre': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'stream_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'tag_list': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'waveform_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['photosong']