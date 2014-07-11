# -*- coding: utf-8 -*-

from collective.directory import _
from five import grok
from plone.supermodel import model
from zope import schema
from plone.namedfile.field import NamedBlobImage
from plone.app.textfield import RichText


class ICard(model.Schema):
    """
    A "Card", directories can contain "Category"s
    """

    title = schema.TextLine(
        title=_(u"Title"),
    )

    sub_title = schema.TextLine(
        title=_(u"Subtitle"),
        required=False,
    )

    description = schema.Text(
        title=_(u"Summary"),
        required=False,
    )

    address = schema.TextLine(
        title=_(u"Address"),
        description=_(u"Street and number"),
        required=False,
    )

    zip_code = schema.Int(
        title=_(u"Zip code"),
        required=False,
    )

    city = schema.TextLine(
        title=_(u"City"),
        required=False,
    )

    phone = schema.TextLine(
        title=_(u"Phone"),
        required=False,
    )

    mobile_phone = schema.TextLine(
        title=_(u"Mobile phone"),
        required=False,
    )

    fax = schema.TextLine(
        title=_(u"Fax"),
        required=False,
    )

    email = schema.TextLine(
        title=_(u"E-mail"),
        required=False,
    )

    website = schema.TextLine(
        title=_(u"Website"),
        required=False,
    )

    schedule = schema.Text(
        title=_(u"Schedule"),
        required=False,
    )

    photo = NamedBlobImage(
        title=_(u"Photo"),
        required=False,
    )

    content = RichText(
        title=_(u"Content"),
        required=False,
    )


class View(grok.View):
    grok.context(ICard)
    grok.require('zope2.View')
