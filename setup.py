#!/usr/bin/env python


from django_bidding import __version__

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages


setup(name='django-bidding',
      description='Django Bidding API',
      author='Dmitry Roitman',
      author_email = "allseeingeye1001@gmail.com",
      url = "https://github.com/dmitryro/django-bidding", 
      version=__version__,

      install_requires=["Django>=1.10.3",
                        "tensorflow>=0.11.0rc2",
                        "keras>=1.2.0"],
       
      packages = [
        "django_bidding",
      ],
      classifiers = [
          "Development Status :: 5 - Production/Stable",
          "Environment :: Web Environment",
          "Framework :: Django :: 1.8",
          "Framework :: Django :: 1.9",
          "Framework :: Django :: 1.10",
          "Framework :: Django",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: BSD License",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
          "Topic :: Software Development :: Libraries",
          "Topic :: Utilities",
      ],
      scripts=['bid_api.py'],
     )
