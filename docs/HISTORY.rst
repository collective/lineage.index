Changelog
=========

0.4 (2012-01-10)
----------------

- PEP8 fixes
  [claytron]

- Use ``IContentish`` instead of ``IATContentType`` to ensure that all
  CMF, AT and Dexterity based content gets indexed properly.
  [claytron]

0.3 (2012-01-08)
----------------

- Make non child site content be indexed as ``None`` so that "main site"
  content can be found via this index also.
  [claytron]

- Make compatible with Plone 4.1
  [jensens]

- Add ``catalog.xml`` and remove ``setuphandlers`` logic.
  [jensens]

- Add ``collective.lineage`` to ``metadata.xml`` dependencies.
  [jensens]

- PEP8 fixes
  [jensens]

- Change extensions of reStructuredText files so they preview correctly.
  [jensens]

- Moved code to GitHub
  [jensens]

0.2 (2011-04-28)
----------------

- Since Lineage's ChildSite is not implementing IPloneSiteRoot anymore,
  changed the indexing reference to implementing INavigationRoot
  [tbesluau]

- For other versions of ATContentType, we need to try and import the interface(s)
  with and without the 's'
  [tbesluau]


0.1b1 (2010-03-16)
------------------

- Initial release
