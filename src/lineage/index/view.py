from Acquisition import aq_parent
from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from plone.memoize.view import memoize_contextless
from plone.uuid.interfaces import IUUID
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory

# Special cases
try:
    from plone.event.interfaces import IOccurrence
except ImportError:
    IOccurrence = None


class ChildsiteView(BrowserView):

    @memoize_contextless
    def titleForKey(self, key):
        """Returns the childsite's title for their vocabulary value.
        """
        util = getUtility(IVocabularyFactory, 'lineage.childsites')
        vocab = util(self.context)
        try:
            return vocab.getTerm(key).title
        except LookupError:
            return key

    def childsiteForContext(self, item):
        """Returns the childsite UUID for a context object by looking up it's
        brain in the catalog.
        """
        childsite = ''
        if IOccurrence and IOccurrence.providedBy(item):
            item = aq_parent(item)
        cat = getToolByName(self.context, 'portal_catalog')
        res = cat.searchResults(UID=IUUID(item, None), path='/')  # TODO: get portal root
        if res:
            childsite = res[0].childsite
        return childsite
