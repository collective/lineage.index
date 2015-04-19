from Products.CMFCore.utils import getToolByName
from collective.lineage.interfaces import IChildSite
from plone.memoize import ram
from zope.interface.declarations import directlyProvides
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary


# cache until next zope restart
# XXX: ideally invalidate when new subsites are created
@ram.cache(lambda *args: ())
def childSiteVocabulary(context):
    """returns the available childsites of the portal
    """
    cat = getToolByName(context, 'portal_catalog')
    brains = cat(
        object_provides=IChildSite.__identifier__,
        sort_on='sortable_title'
    )
    set_brains = []
    terms = []
    for brain in brains:
        val = brain.id
        if val not in set_brains:
            # vocabulary values and tokens must be unique
            set_brains.append(val)
            terms.append(SimpleTerm(value=val, token=val, title=brain.Title))
    return SimpleVocabulary(terms)
directlyProvides(childSiteVocabulary, IVocabularyFactory)
