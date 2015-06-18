# coding: utf-8
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from site_news.views import NewsList, show_item

urlpatterns = [
    url(r'^site_news/$', NewsList.as_view(), name='site-news'),
    url(r'^site_news/(?P<object_id>\d)/', show_item, name='news-item'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(/)*$', TemplateView.as_view(template_name="index.html")),
]
