from Products.Five.browser import BrowserView
from plone.memoize.view import memoize_contextless
from zope.component import getUtility
from zope.schema.interfaces import IVocabularyFactory


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
