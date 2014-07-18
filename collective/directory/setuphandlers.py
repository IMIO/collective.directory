# -*- coding: utf-8 -*-
import logging
from Products.CMFCore.utils import getToolByName
from plone import api

logger = logging.getLogger('collective.directory')


def setupVarious(context):
    if context.readDataFile('collective.directory-default.txt') is None:
        return

    logger.info('Installing')
    portal = context.getSite()

    # Add catalog indexes
    addCatalogIndexes(portal)


def addCatalogIndexes(portal):
    """
    Method to add our wanted indexes to the portal_catalog.
    We couldn't do it in the profile directly, see :
        http://maurits.vanrees.org/weblog/archive/2009/12/catalog
    """
    catalog = getToolByName(portal, 'portal_catalog')
    indexes = catalog.indexes()
    wanted = (('directory', 'KeywordIndex'), )
    indexables = []
    for name, meta_type in wanted:
        if name not in indexes:
            catalog.addIndex(name, meta_type)
            indexables.append(name)
            logger.info("Added %s for field %s.", meta_type, name)
    if len(indexables) > 0:
        logger.info("Indexing new indexes %s.", ', '.join(indexables))
        catalog.manage_reindexIndex(ids=indexables)


def testSetup(context):
    if context.readDataFile('collective_directory_test.txt') is None:
        return
    portal = context.getSite()
    if 'directories' not in portal.objectIds():
        directories_folder = api.content.create(
            container=portal,
            type='Folder',
            id='directories',
            title='Directories'
        )
        make_contents(directories_folder)


def make_contents(container):
    directories = {
        'Sports': {
            'Football': [
                'FC Mornimont',
                'RFC Mornimont',
            ],
            'Hockey': [
                'Mornimont HC',
            ],
        },
        'Assosiations': {
            'Divers': [
                'Scouts',
                'Patro',
            ]
        },
    }
    # import pdb; pdb.set_trace()
    for directory_title in directories.keys():
        directory_folder = api.content.create(
            container=container,
            type="collective.directory.directory",
            title=directory_title,
            id=directory_title.lower()
        )
        for category_title in directories[directory_title].keys():
            category_folder = api.content.create(
                container=directory_folder,
                type="collective.directory.category",
                title=category_title,
                id=category_title.lower()
            )
            for card_title in directories[directory_title][category_title]:
                api.content.create(
                    container=category_folder,
                    type="collective.directory.card",
                    title=card_title,
                    id=card_title.lower()
                )
