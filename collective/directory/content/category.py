# -*- coding: utf-8 -*-

from collective.directory import _
from plone.supermodel import model
from zope import schema


class ICategory(model.Schema):
    """
    A "Category", categories can contain "Card"s
    """

    title = schema.TextLine(
        title=_(u"Category name"),
    )

    description = schema.Text(
        title=_(u"Category summary"),
    )
