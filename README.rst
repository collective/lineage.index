Introduction
============

``lineage.index`` is an addon to `collective.lineage <http://plone.org/products/collective-lineage/>`_ that lets you search for content within a certain childsite.


How does it work?
-----------------

``lineage.index`` registers an index ``childsite`` on all items implementing ``Products.CMFCore.interfaces.IContentish`` (which will be Dexterity based content types).

The childsite's UID can be used to search for content located in this childsite.

When listing items on the main portal, you can use the metadata-column ``childsite`` to indicate which childsites the content has been aggregated from.


How do I use it?
----------------

Once installed, new content gets indexed under the UID of its closest childsite.
Existing content requires a catalog update (see `Installation`_).

You can search for content within a childsite using the index:

.. code-block:: python

    brains = portal_catalog(childsite='9df827df17a94ad0aeda278e9570dc88')

Each brain has a metadata column telling which childsite it's located in:

.. code-block:: python

    >>> brains[0].childsite
    '9df827df17a94ad0aeda278e9570dc88'

If the item comes from the main portal (i.e. not inside a childsite),

- in Plone 5 ``None`` will be indexed.
- in Plone 6 the UID of the portal will be indexed.

This allows you to find only content from the main portal no belonging to any child site:

.. code-block:: python

    >>> brains = portal_catalog(childsite=None)  # Plone 5.x

    >>> from plone.api import portal
    >>> brains = portal_catalog(childsite=portal.get().UID())  # Plone 6+

There's also a vocabulary ``lineage.childsites`` listing the available childsites with their title.

To show the title of the subsite of a brain you can use the utility view:

.. code-block:: html

    <ul tal:define="util context/@@childsite">
        <li tal:repeat="item folderContents">
            <span tal:replace="item/Title">Item 1</span> in
            <span tal:replace="python: util.titleForKey(item.childsite)>Subportal One</span>
        </li>
    </ul>

Installation
============

Install ``lineage.index`` with buildout or pip.
Ensure to have the ZCML included.

In Plone install ``Lineage Index`` in Site Setup, Extensions.

In case you already have childsites and content that shall be indexed go to ZMI, ``portal_catalog``, ``Advanced``.
Then click the ``Update Catalog`` button to populate the index and the catalog metadata (this may take a while).

Gotchas
=======

The vocabulary caches all childsite titles until Zope is restarted.
If you add childsites you need to restart Zope to make them show up in the vocabulary.
