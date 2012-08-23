# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '1.2'

setup(name='upcnet.simpleTask',
      version=version,
      description="",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Plone Team @ UPCnet',
      author_email='plone.team@upcnet.es',
      url='https://github.com/upcnet/upcnet.simpleTask',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['upcnet', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
