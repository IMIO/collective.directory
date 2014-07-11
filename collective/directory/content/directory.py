# -*- coding: utf-8 -*-

from collective.directory import _
from five import grok
from plone.supermodel import model
from zope import schema


grok.templatedir('templates')


class IDirectory(model.Schema):
    """
    A "Directory", directories can contain "Category"s
    """

    title = schema.TextLine(
        title=_(u"Directory name"),
    )

    description = schema.Text(
        title=_(u"Directory summary"),
    )


class Directory():
    pass


class View(grok.View):
    grok.context(IDirectory)
    grok.require('zope2.View')
    grok.template('directory_view')
