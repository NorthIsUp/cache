#!/usr/bin/env python
"""
Flask-Cache
-----------

Adds cache support to your Flask application

"""

from setuptools import setup

setup(
    name='DisqusServiceCache',
    version='0.11.4',
    url='http://github.com/NorthIsUp/cache',
    license='BSD',
    author='Thadeus Burgess',
    author_email='thadeusb@thadeusb.com',
    description='Adds cache support to your disqus-service application',
    long_description=__doc__,
    packages=[
        'cache',
    ],
    zip_safe=False,
    platforms='any',
    test_suite='test_cache',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
