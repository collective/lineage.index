from Products.CMFCore.utils import getToolByName
from collective.lineage.interfaces import IChildSite
import logging

logger = logging.getLogger('lineage.index')


def upgrade_uuid(context):
    """Reindex the childsite index to use UUID instead of id values. This makes
    it possible to have multiple childsites with the same id in different
    paths.
    """
    index_id = 'childsite'

    cat = getToolByName(context, 'portal_catalog')
    cat.manage_clearIndex([index_id])

    # Don't reindex the whole catalog, but only the childsites. These are usaly
    # much less than all the catalog objects together. Thus, this upgrade step
    # runs fast.
    brains = cat(
        object_provides=IChildSite.__identifier__,
        path=cat.__parent__.getPhysicalPath()
    )
    for brain in brains:
        ob = brain.getObject()
        ob.reindexObject(idxs=(index_id,))
        logger.info("Reindex {0} index for {1}.".format(
            index_id,
            ob.absolute_url()
        ))
