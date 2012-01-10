from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary
from zope.schema.interfaces import IVocabularyFactory
from zope.interface.declarations import directlyProvides
from plone.memoize import ram
from Products.CMFCore.utils import getToolByName
from collective.lineage.interfaces import IChildSite

# cache until next zope restart
# XXX: ideally invalidate when new subsites are created


@ram.cache(lambda *args: ())
def childSiteVocabulary(context):
    """returns the available childsites of the portal
    """
    cat = getToolByName(context, 'portal_catalog')

    brains = cat(object_provides=IChildSite.__identifier__,
                 sort_on='sortable_title')
    terms = [SimpleTerm(value=brain.id, token=brain.id, title=brain.Title)
             for brain in brains]
    return SimpleVocabulary(terms)


directlyProvides(childSiteVocabulary, IVocabularyFactory)
