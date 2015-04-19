from Acquisition import aq_base
from Products.CMFCore.interfaces import IContentish
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone import utils
from plone.app.layout.navigation.interfaces import INavigationRoot
from plone.indexer.decorator import indexer


def getNextChildSite(context, portal):
    """Returns the nearest parent object implementing INavigationRoot.
    Code borrowed from plone.app.layout.navigation.root.getNavigationRootObject
    """
    obj = context
    while not INavigationRoot.providedBy(obj) and \
            aq_base(obj) is not aq_base(portal):
        obj = utils.parent(obj)
    return obj


@indexer(IContentish)
def childsite(obj):
    """Return the id of the closest INavigationRoot up the hierarchy or None if
    there is no subsite.
    """
    portal = getToolByName(obj, 'portal_url').getPortalObject()
    navroot = getNextChildSite(obj, portal)

    if navroot == portal:
        # Index None so that you can get all non-child site content
        return None

    return navroot.id