# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest
from django.contrib.sites.models import Site
from site_news.models import NewsItem, NewsItemManager


def _get_site():
    return Site.objects.get_or_create(domain='mock')


class NewsItemTestCase(unittest.TestCase):

    def setUp(self):
        NewsItem.objects.get_or_create(
            title='test item',
            snippet='test snippet',
            section=0,
            site=_get_site()
        )

    def test_get_latest(self):
        """
        """
        self.assertExists(NewsItem.objects.all()[0])
