from setuptools import setup, find_packages
import os

version = '0.1b1'

setup(name='lineage.index',
      version=version,
      description="Adds an index and metadata that allows to search for content of a collective.lineage childsite",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        ],
      keywords='',
      author='Harald Friessnegger',
      author_email='harald at webmeisterei.com',
      url='http://plone.org/products/collective-lineage/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['lineage'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'collective.lineage',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
