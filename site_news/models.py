# -*- coding: utf-8 -*-
from datetime import date

from django.conf import settings
from django.contrib.sites.models import Site
from django.db import models
from django.utils.translation import ugettext_lazy as _

from . import APP_NAME
from .validators import ImageValidator, IMAGE_VALIDATOR_MAX

try:
    from tinymce.models import HTMLField
    HTMLTextField = HTMLField
except ImportError:
    HTMLTextField = models.TextField

SECTION_CHOICES = getattr(settings, "SITE_NEWS_SECTION_CHOICES", ((1, _("Principal")), ))


class NewsItemManager(models.Manager):
    def get_latest(self, section=None, max_items=25):
        if section:
            return self.filter(section=section).order_by('-date', 'title')[:max_items]
        else:
            return self.order_by('-date', 'title')[:max_items]

    def get_latest_by_site(self, site, section=None, max_items=25):
        qs = super(NewsItemManagerPublished, self).get_queryset().filter(site=site)
        if section:
            qs = qs.filter(section=section)
        return qs.order_by('-date', 'title')[:max_items]


class NewsItemManagerPublished(NewsItemManager):
    def get_queryset(self):
        qs = super(NewsItemManagerPublished, self).get_queryset()
        qs = qs.filter(published=True)
        return qs


class NewsItem(models.Model):
    body = HTMLTextField(_(u"Cuerpo"), blank=True)
    date = models.DateField(_(u"Fecha"), default=date.today)
    published = models.BooleanField(_(u"Publicado"), default=True)
    picture = models.ImageField(
        _(u"Foto"), blank=True, null=True,
        validators=[ImageValidator(
            width=1080,
            validation_type=IMAGE_VALIDATOR_MAX,
            allowed_types=('.png', '.jpg', )), ],
        upload_to=(APP_NAME + "/picture"),
        help_text=_(
            u"Usada para ilustrar la noticia. " +
            "Debe ser un archivo png o jpg de 1080 px de ancho como maximo."),
    )
    section = models.PositiveIntegerField(
        _(u"Sección"), choices=SECTION_CHOICES, default=SECTION_CHOICES[0][0])
    site = models.ForeignKey(Site)
    snippet = models.CharField(_(u"Resumen"), max_length=140)
    source_url = models.URLField(_(u"URL de la fuente"), blank=True)
    title = models.CharField(_(u"Título"), max_length=64)

    objects = NewsItemManager()
    objects_published = NewsItemManagerPublished()

    class Meta:
        ordering = ('-date', 'title', )
        unique_together = (('date', 'title'), )
        verbose_name = _(u"Noticia")
        verbose_name_plural = _(u"Noticias")

    def __unicode__(self):
        return u"{0} - {1}".format(self.date, self.title)
