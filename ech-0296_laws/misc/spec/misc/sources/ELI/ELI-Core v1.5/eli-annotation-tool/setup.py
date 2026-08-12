# -*- coding: utf-8 -*-
# Project sponsor is https://ec.europa.eu/isa2/
# License is https://joinup.ec.europa.eu/community/eupl/og_page/eupl

"""setup.py for eli-annotation"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
import os

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

data_patterns = ['static/*.'+ext for ext in 'css js html json xlsx'.split()]
data_patterns += ['static/formats/*.'+ext for ext in ['svg','png']]
data_patterns += ['static/languages/*.'+ext for ext in ['svg','png']]
data_patterns += ['static/forms/*.'+ext for ext in ['json']]
data_patterns += ['xslt/*.'+ext for ext in ['xsl','xml','xhtml']]
data_patterns += ['standard_files/*.'+ext for ext in ['ttl','owl', 'json', 'html']]
for d in 'bootstrap jquery react react-dom react-select'.split():
    data_patterns += ['static/%s/*.js' % d,
                      'static/%s/*.min.css' % d,
                      'static/%s/js/*.js' % d,
                      'static/%s/css/*.min.css' % d,
                      'static/%s/fonts/*' % d,
    ]

setup(
    name='eli-annotation',
    version='1.0.0',
    description='ELI annotation tool',
    long_description=long_description,
    url='https://extranet.logilab.fr/project/eli-annotation',
    author='Logilab for Office des Publications',
    author_email='contact@logilab.fr',
    license='EUPL',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: EUPL',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='eli law europe',

    packages=find_packages(exclude=['contrib', 'docs', 'tests',
                                    'supplied_docs']),

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['bcrypt', 'openpyxl', 'flask', 'flask-login',
                      'lxml', 'rdflib>=4.2.2', 'rdflib-jsonld',
                      'raven', # to connect to sentry
                      'isodate', # rdflib depends on this... remove ? XXX
                      'blinker', # why ? XXX
                      'html5lib>=0.999999999',
                      'python-dateutil' # isodate parser is too permissive
    ],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={},

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    package_data={
        'eli_annotation': data_patterns,
    },
)
