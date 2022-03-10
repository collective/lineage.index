from Products.CMFCore.utils import getToolByName

import logging


logger = logging.getLogger("lineage.index")


def upgrade_uuid(context):
    """Reindex the childsite index to use UUID instead of id values. This makes
    it possible to have multiple childsites with the same id in different
    paths.
    """
    index_id = "childsite"
    cat = getToolByName(context, "portal_catalog")
    cat.delColumn(index_id)
    cat.addColumn(index_id)
    res = (it.getObject() for it in cat.searchResults())  # generator expr.
    for cnt, ob in enumerate(res):
        ob.reindexObject(idxs=(index_id,))
        if cnt % 100 == 0:
            # 100-batch
            logger.info(f"Reindex next batch, starting with {cnt}")
