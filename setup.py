from distutils.core import setup
import os


setup(name='django-site-news',
      version='0.1.1',
      description='Simple news per site application for Django.',
      long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
      author='Maximiliano Cecilia',
      author_email='maxicecilia@gmail.com',
      url='https://github.com/maxicecilia/django_site_news/',
      packages=['site_news'],
      download_url='http://github.com/maxicecilia/django_site_news/downloads/django_site_news-1.0.tar.gz',
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 2.6',
                   'Programming Language :: Python :: 2.7',
                   'Topic :: Utilities'],
      )
