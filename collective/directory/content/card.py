# -*- coding: utf-8 -*-

from collective.directory import _
from five import grok
from plone.supermodel import model
from zope import schema


class ICard(model.Schema):
    """
    A "Card", directories can contain "Category"s
    """

    title = schema.TextLine(
        title=_(u"Card name"),
    )

    description = schema.Text(
        title=_(u"Card summary"),
    )


class View(grok.View):
    grok.context(ICard)
    grok.require('zope2.View')
