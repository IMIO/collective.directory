# -*- coding: utf-8 -*-
from Products.Five import BrowserView
import json
from collective.geo.leaflet.utils import get_marker_image
import logging
from Products.CMFCore.utils import getToolByName
logger = logging.getLogger('collective.directory.brower.jsonview')


class JsonDirectory(BrowserView):

    # index = ViewPageTemplateFile("jsonview.pt")
    categories = []

    def __call__(self):
        self.request.RESPONSE.setHeader(
            'Content-Type',
            'application/javascript; charset=utf-8')
        return self.get_categories()

    @property
    def portal_catalog(self):
        return getToolByName(self.context, 'portal_catalog')

    def get_brain(self):
        querydict = {}
        querydict['path'] = {'query': '/'.join(self.context.getPhysicalPath())}
        #querydict['portal_type'] = 'collective.directory.category'
        #querydict['depth'] = 1
        return self.portal_catalog(querydict)

    def get_categories(self):
        categories = {}
        for brain in self.get_brain():
            if brain.zgeo_geometry:
                marker = {}
                cat = brain.collective_directory_category
                isaCard = 'collective.direcotry.category'
                if not cat:
                    obj = brain.getObject()
                    cat = obj.aq_parent.id
                    # Be Careful : If a card is in another card, obj.aq_parent.portal_type is a card so, cat ID is not a key in self.context
                    isaCard = obj.aq_parent.portal_type
                    logger.info("Obj: {0} not good for performance, start collective.directory upgradesteps 2".format(obj.id))
                if isaCard == 'collective.directory.category':
                    geom = {'type': brain.zgeo_geometry['type'],
                            'coordinates': brain.zgeo_geometry['coordinates']}
                    marker['geom'] = geom
                    marker['style'] = brain.collective_geo_styles
                    marker['title'] = brain.Title
                    marker['description'] = brain.Description
                    marker['category'] = cat
                    marker['url'] = brain.getURL()
                    # Attention plante quand sous carte dans carte.
                    # if "lafforgue-jean-philippe" in cat:
                    #    import ipdb
                    #    ipdb.set_trace()
                    if cat not in categories.keys():
                        categories[cat] = {}
                        categories[cat]['title'] = self.context[cat].title
                        img_url = get_marker_image(
                            self.context,
                            marker['style'].get('marker_image'))
                        categories[cat]['img_url'] = img_url
                        categories[cat]['markers'] = []
                    categories[cat]['markers'].append(marker)
        return "var data_categories = {0}".format(json.dumps(categories, sort_keys=True))
