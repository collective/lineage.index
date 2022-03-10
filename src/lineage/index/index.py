from Acquisition import aq_base
from collective.lineage.interfaces import IChildSite
from plone.dexterity.interfaces import IDexterityContent
from plone.indexer.decorator import indexer
from plone.uuid.interfaces import IUUID
from Products.CMFCore.interfaces import IContentish
from Products.CMFPlone import utils

import plone.api


def getNextChildSite(context, portal):
    """Returns the nearest parent object implementing IChildSite.
    Code borrowed from plone.app.layout.navigation.root.getNavigationRootObject
    """
    obj = context
    while not IChildSite.providedBy(obj) and aq_base(obj) is not aq_base(portal):
        obj = utils.parent(obj)
        if obj is None:
            return
    return obj


@indexer(IContentish)
def childsite(obj):
    """Return the uuid of the closest childsite up the hierarchy or None if
    there is no subsite.
    """
    portal = plone.api.portal.get()
    childsite = getNextChildSite(obj, portal)

    if childsite == portal:
        if IDexterityContent.providedBy(portal):
            return IUUID(portal)
        else:
            return None

    if childsite is None:
        raise AttributeError("no childsite found")

    return IUUID(childsite)
