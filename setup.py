# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup

version = '0.5'

setup(
    name='lineage.index',
    version=version,
    description="Adds an index and metadata that allows to search for "
                "content of a collective.lineage childsite",
    long_description='{0}/n{1}'.format(
        open("README.rst").read(),
        open("CHANGES.rst").read()
    ),
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
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['lineage'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'collective.lineage',
        'plone.api',
    ],
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
