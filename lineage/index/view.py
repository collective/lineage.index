from Products.Five.browser import BrowserView
from zope.schema.interfaces import IVocabularyFactory
from zope.component import getUtility
from plone.memoize.view import memoize_contextless


class ChildsiteView(BrowserView):

    @memoize_contextless
    def titleForKey(self, key):
        """returns the childsite's title for their vocabulary value.
        """
        util = getUtility(IVocabularyFactory, 'lineage.childsites')
        vocab = util(self.context)
        try:
            return vocab.getTerm(key).title
        except LookupError:
            return key
