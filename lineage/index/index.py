from plone.indexer.decorator import indexer
try:
    from Products.ATContentTypes.interfaces.interfaces import IATContentType
except:
    from Products.ATContentTypes.interface.interfaces import IATContentType
from Products.CMFCore.utils import getToolByName
from plone.app.layout.navigation.interfaces import INavigationRoot
from Acquisition import aq_base
from Products.CMFPlone import utils


def getNextChildSite(context, portal):
    """returns the nearest parent object implementing INavigationRoot.

    code borrowed from plone.app.layout.navigation.root.getNavigationRootObject
    """

    obj = context
    while not INavigationRoot.providedBy(obj) and \
                    aq_base(obj) is not aq_base(portal):
        obj = utils.parent(obj)
    return obj


@indexer(IATContentType)
def childsite(obj):
    """return the id of the closest INavigationRoot up the hierarchy or None if
    there is no subsite
    """
    portal = getToolByName(obj, 'portal_url').getPortalObject()
    navroot = getNextChildSite(obj, portal)

    if navroot == portal:
        # Index None so that you can get all non-child site content
        return None

    return navroot.id
