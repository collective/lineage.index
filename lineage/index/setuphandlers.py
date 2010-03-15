# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
from plone.app.workflow.browser.sharing import SharingView
from Products.CMFEditions.setuphandlers import DEFAULT_POLICIES



def importVarious(context):
    """Miscellaneous steps import handle
    """

    # Ordinarily, GenericSetup handlers check for the existence of XML files.
    # Here, we are not parsing an XML file, but we use this text file as a
    # flag to check that we actually meant for this import step to be run.
    if context.readDataFile('lineage.index_various.txt') is None:
        return

    portal = context.getSite()
    createIndexes(portal)



def createIndexes(portal):
    """We don't use GS catalog.xml to create indexes since it re-creates them every product
    reinstall.
    this needs to be done until this bug is resolved: https://bugs.launchpad.net/zope-cmf/+bug/161682
    """

    catalog = getToolByName(portal, 'portal_catalog')

    if 'childsite' not in catalog.indexes():
        catalog.addIndex('childsite', 'FieldIndex')


