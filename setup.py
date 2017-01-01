#!/usr/bin/env python


try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages


setup(name='django-bidding',
      version='1.0',
      description='Django Bidding API',
      author='Dmitry Roitman',
      install_requires=["Django>=1.10.3",
                        "tensorflow>=0.11.0rc2",
                        "keras>=1.2.0"],
      packages=find_packages(),
      scripts=['bid_api.py'],
     )
