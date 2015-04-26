from Acquisition import aq_base
from Products.CMFCore.interfaces import IContentish
from Products.CMFPlone import utils
from collective.lineage.interfaces import IChildSite
from plone.indexer.decorator import indexer
from plone.uuid.interfaces import IUUID
import plone.api


def getNextChildSite(context, portal):
    """Returns the nearest parent object implementing IChildSite.
    Code borrowed from plone.app.layout.navigation.root.getNavigationRootObject
    """
    obj = context
    while not IChildSite.providedBy(obj) and\
            aq_base(obj) is not aq_base(portal):
        obj = utils.parent(obj)
    return obj


@indexer(IContentish)
def childsite(obj):
    """Return the uuid of the closest childsite up the hierarchy or None if
    there is no subsite.
    """
    portal = plone.api.portal.get()
    childsite = getNextChildSite(obj, portal)

    if childsite == portal:
        # Index None so that you can get all non-child site content
        return None

    return IUUID(childsite)
