# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing M2M table for field songs on 'Tag'
        db.delete_table(db.shorten_name(u'photosong_tag_songs'))

        # Adding M2M table for field photos on 'Tag'
        m2m_table_name = db.shorten_name(u'photosong_tag_photos')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tag', models.ForeignKey(orm[u'photosong.tag'], null=False)),
            ('photo', models.ForeignKey(orm[u'photosong.photo'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tag_id', 'photo_id'])


        # Changing field 'Song.title'
        db.alter_column(u'photosong_song', 'title', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

    def backwards(self, orm):
        # Adding M2M table for field songs on 'Tag'
        m2m_table_name = db.shorten_name(u'photosong_tag_songs')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tag', models.ForeignKey(orm[u'photosong.tag'], null=False)),
            ('song', models.ForeignKey(orm[u'photosong.song'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tag_id', 'song_id'])

        # Removing M2M table for field photos on 'Tag'
        db.delete_table(db.shorten_name(u'photosong_tag_photos'))


        # Changing field 'Song.title'
        db.alter_column(u'photosong_song', 'title', self.gf('django.db.models.fields.CharField')(default='title', max_length=200))

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
            'genre': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'photo'", 'to': u"orm['photosong.Photo']"}),
            'soundcloud_id': ('django.db.models.fields.IntegerField', [], {}),
            'stream_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'tag_list': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'waveform_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'photosong.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'photos': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['photosong.Photo']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['photosong']