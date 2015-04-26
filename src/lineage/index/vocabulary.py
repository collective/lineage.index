from Products.CMFCore.utils import getToolByName
from collective.lineage.interfaces import IChildSite
from plone.memoize import ram
from zope.interface.declarations import directlyProvides
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary
import plone.api


# cache until next zope restart
# XXX: ideally invalidate when new subsites are created
@ram.cache(lambda *args: ())
def childSiteVocabulary(context):
    """returns the available childsites of the portal
    """
    cat = getToolByName(context, 'portal_catalog')
    portal = plone.api.portal.get()
    brains = cat(
        object_provides=IChildSite.__identifier__,
        path=portal.getPhysicalPath(),
        sort_on='sortable_title'
    )
    terms = [
        SimpleTerm(value=brain.UID, token=brain.UID, title=brain.Title)
        for brain in brains
    ]
    return SimpleVocabulary(terms)

directlyProvides(childSiteVocabulary, IVocabularyFactory)
