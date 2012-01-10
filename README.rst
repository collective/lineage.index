Introduction
============

``lineage.index`` is an addon to `collective.lineage`_ that lets you
search for content within a certain childsite.

How does it work?
-----------------

``lineage.index`` registers an index ``childsite`` on all items
implementing ``Products.CMFCore.interfaces.IContentish`` (which will be
all Archetypes and Dexterity based content types).

The childsite's id can be used to search for content located in this
childsite.

When listing items on the main portal, you can use the metadata-column
``childsite`` to indicate which childsites the content has been
aggregated from.

How do I use it?
----------------

Once installed, new content gets indexed under the id of its closest
childsite. Existing content requires a catalog update (see
`Installation`_).

You can search for content within a childsite using the index::

    brains = portal_catalog(childsite='subsite1')

Each brain has a metadata column telling which childsite it's located
in::

    >>> brains[0].childsite
    'subsite1'

If the item comes from the main portal (i.e. not inside a childsite),
``None`` will be indexed. This allows you to find only content from the
main portal::

    >>> brains = portal_catalog(childsite=None)
    >>> brains[0].childsite is None
    True

There's also a vocabulary ``lineage.childsites`` listing the available
childsites with their title.

To show the title of the subsite of a brain you can use the utility
view::

    <ul tal:define="util context/@@childsite">
        <li tal:repeat="item folderContents">
            <span tal:replace="item/Title">Item 1</span> in
            <span tal:replace="python: util.titleForKey(item.childsite)>Subportal One</span>
        </li>
    </ul>

Installation
============

Simply add ``lineage.index`` to your buildout eggs (no zcml slug is
needed thanks to z3c.autoinclude).

Quickinstall ``Lineage Index``.

In case you already have childsites and content that shall be indexed
go to ``portal_catalog/manage_catalogAdvanced`` and click the
``Update Catalog`` button to populate the index and the catalog
metadata.

Gotchas
=======

The vocabulary caches all childsite titles until zope is restarted.
If you add childsites you need to restart zope to make them show up
in the vocabulary.

.. _`collective.lineage`: http://plone.org/products/collective-lineage/

