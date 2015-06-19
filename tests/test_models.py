# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import unittest
from django.contrib.sites.models import Site
from site_news.models import NewsItem, NewsItemManager


def _get_site():
    return Site.objects.get_or_create(domain='mock')[0]


class NewsItemTestCase(unittest.TestCase):

    def setUp(self):
        from django.core.management import call_command
        call_command('loaddata', 'tests/fixtures/test_data.json', verbosity=0)

    def test_get_latest(self):
        """
            Get all items, ordered by dates.
        """
        qs = NewsItem.objects.get_latest()
        self.assertEqual(qs.count(), 12)
        self.assertTrue(qs[0].date >= qs[1].date)
        self.assertTrue(qs[1].date >= qs[2].date)

    def test_get_latest_with_max_items(self):
        """
            Get all items, ordered by dates and trimmed to max_items.
        """
        qs = NewsItem.objects.get_latest(max_items=4)
        self.assertEqual(qs.count(), 4)
        self.assertTrue(qs[0].date >= qs[1].date)
        self.assertTrue(qs[1].date >= qs[2].date)

    def test_get_latest_by_site(self):
        """
            Get all items for given site, ordered by dates.
        """
        qs = NewsItem.objects.get_latest_by_site(
            site=Site.objects.get(domain='buytowels.com'))
        self.assertEqual(qs.count(), 6)
        self.assertTrue(qs[0].date >= qs[1].date)
        self.assertTrue(qs[1].date >= qs[2].date)

    def test_get_latest_by_site_with_max_items(self):
        """
            Get all items for given site, ordered by dates and trimmed to max_items.
        """
        qs = NewsItem.objects.get_latest_by_site(
            site=Site.objects.get(domain='buytowels.com'),
            max_items=3)
        self.assertEqual(qs.count(), 3)
        self.assertTrue(qs[0].date >= qs[1].date)
        self.assertTrue(qs[1].date >= qs[2].date)

    def test_get_latest_published(self):
        """
            Get published items, ordered by dates.
        """
        qs = NewsItem.objects_published.get_latest()
        self.assertEqual(qs.count(), 7)
        self.assertTrue(qs[0].date >= qs[1].date)
        self.assertTrue(qs[1].date >= qs[2].date)

    def test_get_latest_published_with_max_items(self):
        """
            Get published items, ordered by dates and trimmed to max_items.
        """
        qs = NewsItem.objects_published.get_latest(max_items=4)
        self.assertEqual(qs.count(), 4)
        self.assertTrue(qs[0].date >= qs[1].date)
        self.assertTrue(qs[1].date >= qs[2].date)

    def test_get_latest_published_by_site(self):
        """
            Get published items for given site, ordered by dates.
        """
        qs = NewsItem.objects_published.get_latest_by_site(
            site=Site.objects.get(domain='buytowels.com'))
        self.assertEqual(qs.count(), 6)
        self.assertTrue(qs[0].date >= qs[1].date)
        self.assertTrue(qs[1].date >= qs[2].date)

    def test_get_latest_published_by_site_with_max_items(self):
        """
            Get published items for given site, ordered by dates and trimmed to max_items.
        """
        qs = NewsItem.objects_published.get_latest_by_site(
            site=Site.objects.get(domain='buytowels.com'),
            max_items=3)
        self.assertEqual(qs.count(), 3)
        self.assertTrue(qs[0].date >= qs[1].date)
        self.assertTrue(qs[1].date >= qs[2].date)