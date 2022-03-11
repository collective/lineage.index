from setuptools import find_packages
from setuptools import setup


version = "1.0"
short_description = (
    "Adds an index and metadata that allows to search for "
    "content of a collective.lineage childsite"
)
long_description = "\n\n".join(
    [
        open("README.rst").read(),
        open("CHANGES.rst").read(),
    ]
)


setup(
    name="lineage.index",
    version=version,
    description=short_description,
    long_description=long_description,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 5.2",
        "Framework :: Plone :: 6.0",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",

    ],
    keywords="",
    author="Harald Friessnegger",
    author_email="harald@webmeisterei.com",
    url="http://github/com/collective/lineage.index",
    license="GPL",
    packages=find_packages("src"),
    package_dir={"": "src"},
    namespace_packages=["lineage"],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "setuptools",
        "collective.lineage",
        "plone.api",
    ],
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
