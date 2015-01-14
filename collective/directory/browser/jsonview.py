# -*- coding: utf-8 -*-
try:
    from shapely.geometry import asShape
except:
    from pygeoif.geometry import as_shape as asShape

import geojson
import json
from collective.geo.json.browser.jsonview import JsonFolderDocument
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class JsonDirectoryDocument(JsonFolderDocument):

    index = ViewPageTemplateFile("jsonview.pt")

    def __call__(self):
        return self.index()

    def get_geojsons(self):
        json_result = []
        for brain in self.get_brain():
            if brain.zgeo_geometry:
                self.styles = brain.collective_geo_styles
                geom = {'type': brain.zgeo_geometry['type'],
                        'coordinates': brain.zgeo_geometry['coordinates']}
                if geom['coordinates']:
                    if geom['type']:
                        classes = geom['type'].lower() + ' '
                    else:
                        classes = ''
                    classes += brain.getPath().split('/')[-2].replace('.', '-')
                    json_result.append(
                        geojson.Feature(
                            id=brain.id.replace('.', '-'),
                            geometry=asShape(geom),
                            style=self._get_style(geom),
                            properties={
                                "title": brain.Title,
                                "description": brain.Description,
                                "category": brain.collective_directory_category,
                                "style": self._get_style(geom),
                                "url": brain.getURL(),
                                "classes": classes,
                            }
                        )
                    )
        json_list = arrange_json_by_category(json_result)
        geojson_list = []
        for index, value in json_list.items():
            feature_collection = {}
            feature_collection['geojson'] = geojson.dumps(geojson.FeatureCollection(value))
            feature_collection['title'] = self.context[index].title
            #geojson_list.append(json.loads(geojson.dumps(feature_collection)))
            geojson_list.append(feature_collection)
        self.request.RESPONSE.setHeader('Content-Type',
                                        'application/json; charset=utf-8')
        return geojson_list


def arrange_json_by_category(json_result):
    json_dict = {}
    for result in json_result:
        value = []
        if result['properties']['category'] in json_dict.keys():
            value = json_dict[result['properties']['category']]
        value.append(result)
        json_dict[result['properties']['category']] = value
    return json_dict
