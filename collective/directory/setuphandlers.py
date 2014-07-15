# -*- coding: utf-8 -*-
from plone import api


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
                card = api.content.create(
                    container=category_folder,
                    type="collective.directory.card",
                    title=card_title,
                    id=card_title.lower()
                )
