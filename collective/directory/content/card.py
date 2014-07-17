# -*- coding: utf-8 -*-
from five import grok
from plone.directives import dexterity
from plone.app.textfield import RichText
from plone.namedfile.field import NamedBlobImage
from plone.supermodel import model
from zope import schema

from collective.directory import _
from collective.schedulefield.schedule import Schedule


grok.templatedir('templates')


class ICard(model.Schema):
    """
    A "Card", directories can contain "Category"s
    """

    subtitle = schema.TextLine(
        title=_(u"Subtitle"),
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

    schedule = Schedule(
        title=_(u"Schedule"),
        required=False)

    photo = NamedBlobImage(
        title=_(u"Photo"),
        required=False,
    )

    content = RichText(
        title=_(u"Content"),
        required=False,
    )


class DetailCard(dexterity.DisplayForm):
    grok.context(ICard)
    grok.require('zope2.View')


class ListingCardsMixin():

    def getSubCards(self):
        portal_type = "collective.directory.card"
        results = self.context.portal_catalog.searchResults(
            portal_type=portal_type,
            path={'query': '/'.join(self.context.getPhysicalPath())},
            review_state='published',
            sort_on='sortable_title')
        results = [result.getObject() for result in results]

        # remove actual card because path get the actual too, not only the
        # containing objects
        if self.context.portal_type == portal_type:
            results.remove(self.context)

        return results


class ListingCards(ListingCardsMixin, dexterity.DisplayForm):
    grok.context(ICard)
    grok.require('zope2.View')
