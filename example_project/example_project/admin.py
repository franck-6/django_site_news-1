# -*- coding: utf-8 -*-
from django.contrib import admin
from site_news.admin import NewsItemAdmin
from site_news.models import NewsItem

admin.site.register(NewsItem, NewsItemAdmin)
