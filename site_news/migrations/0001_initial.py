# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'NewsItem'
        db.create_table(u'site_news_newsitem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('body', self.gf('tinymce.models.HTMLField')(blank=True)),
            ('date', self.gf('django.db.models.fields.DateField')(default=datetime.date.today)),
            ('published', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('section', self.gf('django.db.models.fields.PositiveIntegerField')(default=1)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
            ('snippet', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('source_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal(u'site_news', ['NewsItem'])

        # Adding unique constraint on 'NewsItem', fields ['date', 'title']
        db.create_unique(u'site_news_newsitem', ['date', 'title'])


    def backwards(self, orm):
        # Removing unique constraint on 'NewsItem', fields ['date', 'title']
        db.delete_unique(u'site_news_newsitem', ['date', 'title'])

        # Deleting model 'NewsItem'
        db.delete_table(u'site_news_newsitem')


    models = {
        u'site_news.newsitem': {
            'Meta': {'ordering': "('-date', 'title')", 'unique_together': "(('date', 'title'),)", 'object_name': 'NewsItem'},
            'body': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'section': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'snippet': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'source_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['site_news']