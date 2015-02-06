django_site_news
====================

Simple django app for displaying news and/or posts. Supports custom snippets and images.


### Installation
Install using pip
```
$ pip install -e git://github.com/maxicecilia/django_site_news.git@0.1.0#egg=site_news
```
Add site_news to settings.py
```
INSTALLED_APPS = (
    ...
    'site_news',
    ...
)
```
Update DB models
```
$ python manage.py syncdb --migrate  # Django < 1.7 + South
$ python manage.py migrate  # Django 1.7+
```

### Usage
There are two options to manage the news in the admin site, depending on your needs.
* Full News Admin


```python
from django.contrib import admin
from site_news.admin import NewsItemAdmin
from site_news.models import NewsItem

admin.site.register(NewsItem, NewsItemAdmin)
```

* Simple News Admin

```python
from django.contrib import admin
from site_news.admin import NewsItemSimplifiedAdmin
from site_news.models import NewsItem

admin.site.register(NewsItem, NewsItemSimplifiedAdmin)
```

### Managers
You have available two News managers, the default *objects* and *objects_published*, that filters only through published items.

```python
#  You can replace this:
news_items = NewsItem.objects.filter(section=section, published=True).order_by('-date', 'title')

# with this:
news_items = NewsItem.objects_published.get_latest(section=section)
```

### Settings
You can override the default sections in your settings.py using:

```python
SITE_NEWS_SECTION_CHOICES = ((1, 'Main Content'), (2, 'Header'), (3, 'Aside'))
```
django_site_news
====================

Simple django app for displaying news and/or posts. Supports custom snippets and images.


### Installation
Install using pip
```
$ pip install -e git://github.com/maxicecilia/django_site_news.git@0.1.0#egg=site_news
```
Add site_news to settings.py
```
INSTALLED_APPS = (
    ...
    'site_news',
    ...
)
```
Update DB models
```
$ python manage.py syncdb --migrate  # Django < 1.7 + South
$ python manage.py migrate  # Django 1.7+
```

### Usage
There are two options to manage the news in the admin site, depending on your needs.
* Full News Admin


```python
from django.contrib import admin
from site_news.admin import NewsItemAdmin
from site_news.models import NewsItem

admin.site.register(NewsItem, NewsItemAdmin)
```

* Simple News Admin

```python
from django.contrib import admin
from site_news.admin import NewsItemSimplifiedAdmin
from site_news.models import NewsItem

admin.site.register(NewsItem, NewsItemSimplifiedAdmin)
```

### Managers
You have available two News managers, the default *objects* and *objects_published*, that filters only through published items.

```python
#  You can replace this:
news_items = NewsItem.objects.filter(section=section, published=True).order_by('-date', 'title')

# with this:
news_items = NewsItem.objects_published.get_latest(section=section)
```

### Settings
You can override the default sections in your settings.py using:

```python
SITE_NEWS_SECTION_CHOICES = ((1, 'Main Content'), (2, 'Header'), (3, 'Aside'))
```
