# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tag'
        db.create_table(u'photosong_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'photosong', ['Tag'])

        # Adding M2M table for field name on 'Tag'
        m2m_table_name = db.shorten_name(u'photosong_tag_name')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('tag', models.ForeignKey(orm[u'photosong.tag'], null=False)),
            ('song', models.ForeignKey(orm[u'photosong.song'], null=False))
        ))
        db.create_unique(m2m_table_name, ['tag_id', 'song_id'])


    def backwards(self, orm):
        # Deleting model 'Tag'
        db.delete_table(u'photosong_tag')

        # Removing M2M table for field name on 'Tag'
        db.delete_table(db.shorten_name(u'photosong_tag_name'))


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
            'stream_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'tag_list': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'waveform_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'photosong.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['photosong.Song']", 'symmetrical': 'False'})
        }
    }

    complete_apps = ['photosong']