from collective.lineage.interfaces import IChildSite
from plone.dexterity.interfaces import IDexterityContent
from plone.memoize import ram
from zope.interface import provider
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary

import plone.api


# cache until next zope restart
# XXX: ideally invalidate when new subsites are created
@ram.cache(lambda *args: ())
@provider(IVocabularyFactory)
def childSiteVocabulary(context):
    """returns the available childsites of the portal"""
    portal = plone.api.portal.get()
    if IDexterityContent.providedBy(portal):
        terms = [SimpleTerm(value=portal.UID(), token=portal.UID(), title="Root Portal")]
    else:
        terms = []
    brains = plone.api.content.find(
        object_provides=IChildSite.__identifier__,
        path=portal.getPhysicalPath(),
        sort_on="sortable_title",
    )
    terms += [
        SimpleTerm(value=brain.UID, token=brain.UID, title=brain.Title)
        for brain in brains
    ]
    return SimpleVocabulary(terms)
