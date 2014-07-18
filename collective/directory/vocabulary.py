# -*- coding: utf-8 -*-
from binascii import b2a_qp
from zope.interface import implements
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary
from zope.site.hooks import getSite

from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import safe_unicode


class BasePortalTypeVocabulary(object):
    """Vocabulary factory depending on portal_type"""
    implements(IVocabularyFactory)
    portal_type = ''

    def __call__(self, context, query=None):
        site = getSite()
        self.catalog = getToolByName(site, "portal_catalog", None)
        if self.catalog is None:
            return SimpleVocabulary([])

        brains = self.catalog.searchResults(portal_type=self.portal_type)
        items = []
        for brain in brains:
            obj = brain.getObject()
            items.append(SimpleTerm(obj.id, obj.id, obj.title))
        return SimpleVocabulary(items)


class DirectoryVocabulary(BasePortalTypeVocabulary):
    """Vocabulary factory listing all directory"""
    portal_type = 'collective.directory.directory'


class CategoryVocabulary(BasePortalTypeVocabulary):
    """Vocabulary factory listing all category"""
    portal_type = 'collective.directory.category'


DirectoryVocabularyFactory = DirectoryVocabulary()
CategoryVocabularyFactory = CategoryVocabulary()
