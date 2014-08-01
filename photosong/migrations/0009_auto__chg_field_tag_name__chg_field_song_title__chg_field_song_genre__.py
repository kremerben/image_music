# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Tag.name'
        db.alter_column(u'photosong_tag', 'name', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'Song.title'
        db.alter_column(u'photosong_song', 'title', self.gf('django.db.models.fields.CharField')(max_length=300, null=True))

        # Changing field 'Song.genre'
        db.alter_column(u'photosong_song', 'genre', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Song.tag_list'
        db.alter_column(u'photosong_song', 'tag_list', self.gf('django.db.models.fields.CharField')(max_length=500, null=True))

    def backwards(self, orm):

        # Changing field 'Tag.name'
        db.alter_column(u'photosong_tag', 'name', self.gf('django.db.models.fields.CharField')(max_length=120))

        # Changing field 'Song.title'
        db.alter_column(u'photosong_song', 'title', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Song.genre'
        db.alter_column(u'photosong_song', 'genre', self.gf('django.db.models.fields.CharField')(max_length=120, null=True))

        # Changing field 'Song.tag_list'
        db.alter_column(u'photosong_song', 'tag_list', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

    models = {
        u'photosong.photo': {
            'Meta': {'object_name': 'Photo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'photosong.song': {
            'Meta': {'object_name': 'Song'},
            'artwork_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'download_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'genre': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'photo'", 'to': u"orm['photosong.Photo']"}),
            'soundcloud_id': ('django.db.models.fields.IntegerField', [], {}),
            'stream_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'tag_list': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'waveform_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'photosong.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'photos': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'photo_tag'", 'symmetrical': 'False', 'to': u"orm['photosong.Photo']"})
        }
    }

    complete_apps = ['photosong']