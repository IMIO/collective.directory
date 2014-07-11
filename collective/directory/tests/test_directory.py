# -*- coding: utf-8 -*-

import unittest

from zope.component import createObject
from zope.component import queryUtility

from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles

from plone.dexterity.interfaces import IDexterityFTI

from collective.directory.content.directory import IDirectory
from collective.directory.testing import COLLECTIVE_DIRECTORY_INTEGRATION_TESTING


class TestDirectoryIntegration(unittest.TestCase):
    """Integration test for the Directory type
    """

    layer = COLLECTIVE_DIRECTORY_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.portal.invokeFactory('Folder', 'test-folder')
        self.folder = self.portal['test-folder']

    def test_adding(self):
        self.folder.invokeFactory('collective.directory.directory', 'directory1')
        d1 = self.folder['directory1']
        self.assertTrue(IDirectory.providedBy(d1))

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='collective.directory.directory')
        self.assertNotEquals(None, fti)

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='collective.directory.directory')
        schema = fti.lookupSchema()
        self.assertEqual(IDirectory, schema)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='collective.directory.directory')
        factory = fti.factory
        new_object = createObject(factory)
        self.assertTrue(IDirectory.providedBy(new_object))

    def test_view(self):
        self.folder.invokeFactory('collective.directory.directory', 'directory1')
        d1 = self.folder['directory1']
        view = d1.restrictedTraverse('@@view')
        self.assertNotEquals(None, view)


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
