from Products.Five.browser import BrowserView
from zope.schema.interfaces import IVocabularyFactory
from zope.component._api import getUtility

class ChildsiteView(BrowserView):

    def titleForKey(self, key):
        """returns the childsite's title for their vocabulary value
        """
        vocab = getUtility(IVocabularyFactory, 'lineage.childsites')(self.context)
        try:
            return vocab.getTerm(key).title
        except LookupError:
            return key

