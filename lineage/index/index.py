from plone.indexer.decorator import indexer
from Products.ATContentTypes.interfaces.interfaces import IATContentType
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.interfaces.siteroot import IPloneSiteRoot
from Acquisition import aq_base
from Products.CMFPlone import utils


def getNextChildSite(context, portal):
    """returns the nearest parent object implementing IPloneSiteRoot.

    code borrowed from plone.app.layout.navigation.root.getNavigationRootObject
    """

    obj = context
    while not IPloneSiteRoot.providedBy(obj) and aq_base(obj) is not aq_base(portal):
        obj = utils.parent(obj)
    return obj


@indexer(IATContentType)
def childsite(obj):
    """return the id of the closest IPloneSiteRoot up the hierarchy or None if there is no subsite
    """
    portal = getToolByName(obj, 'portal_url').getPortalObject()
    navroot = getNextChildSite(obj, portal)

    if navroot == portal:
        # ZCatalog seems to use [] as a maker for "don't index object under this value"
        return []

    return navroot.id
