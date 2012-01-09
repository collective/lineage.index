from setuptools import setup, find_packages
import os

version = '0.4'

setup(name='lineage.index',
      version=version,
      description="Adds an index and metadata that allows to search for "
                  "content of a collective.lineage childsite",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.rst")).read(),
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
      author_email='harald at webmeisterei dot com',
      url='http://pypi.python.org/pypi/lineage.index',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['lineage'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'collective.lineage',
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
