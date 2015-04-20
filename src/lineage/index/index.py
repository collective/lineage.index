from Acquisition import aq_base
from Products.CMFCore.interfaces import IContentish
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone import utils
from collective.lineage.interfaces import IChildSite
from plone.indexer.decorator import indexer
from plone.uuid.interfaces import IUUID


def getNextChildSite(context, portal):
    """Returns the nearest parent object implementing INavigationRoot.
    Code borrowed from plone.app.layout.navigation.root.getNavigationRootObject
    """
    obj = context
    while not IChildSite.providedBy(obj) and\
            aq_base(obj) is not aq_base(portal):
        obj = utils.parent(obj)
    return obj


@indexer(IContentish)
def childsite(obj):
    """Return the id of the closest INavigationRoot up the hierarchy or None if
    there is no subsite.
    """
    portal = getToolByName(obj, 'portal_url').getPortalObject()
    childsite = getNextChildSite(obj, portal)

    if childsite == portal:
        # Index None so that you can get all non-child site content
        return None

    return IUUID(childsite)
