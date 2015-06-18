# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext as _
from django.views.generic import ListView

from models import NewsItem, SECTION_CHOICES


EMPTY_NEWS_PAGE = getattr(settings, 'SITE_NEWS_EMPTY_NEWS_PAGE', '')


def show_item(request, object_id, template='site_news/item.html', extra_context=None):
    try:
        object_id = NewsItem._meta.pk.to_python(object_id)
        obj = NewsItem.objects_published.get(pk=object_id)
    except (ObjectDoesNotExist, ValidationError):
        raise Http404(_(u"La noticia no existe"))
    context = {
        'obj': obj,
    }
    context.update(extra_context or {})
    context_instance = RequestContext(request)
    return render_to_response(template, context, context_instance=context_instance)


class NewsList(ListView):
    '''
        Returns all published news for the current site and section (if any).
    '''
    context_object_name = 'news'
    template_name = 'site_news/list.html'

    def get_template_names(self):
        if self.kwargs and 'template_name' in self.kwargs:
            return [self.kwargs['template_name']]
        return [self.template_name]

    def get_queryset(self):
        current_site = self.request.site if 'site' in self.request \
            else get_current_site(self.request)
        if self.kwargs and 'section' in self.kwargs:
            try:
                section = [x[0] for x in SECTION_CHOICES
                           if x[1].lower() == self.kwargs['section'].lower()][0]
            except IndexError:
                section = None
            queryset = NewsItem.objects_published.get_latest_by_site(
                site=current_site, section=section)
        else:
            queryset = NewsItem.objects_published.get_latest_by_site(
                site=current_site)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(NewsList, self).get_context_data(**kwargs)
        context['section'] = self.kwargs.get('section', _('Noticias'))
        return context

    def dispatch(self, request, *args, **kwargs):
        if len(self.get_queryset()) == 0 and EMPTY_NEWS_PAGE != '':
            return HttpResponseRedirect(EMPTY_NEWS_PAGE)
        else:
            return super(NewsList, self).dispatch(request, *args, **kwargs)
