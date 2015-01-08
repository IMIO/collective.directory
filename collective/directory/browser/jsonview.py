# -*- coding: utf-8 -*-
try:
    from shapely.geometry import asShape
except:
    from pygeoif.geometry import as_shape as asShape

import geojson
from collective.geo.json.browser.jsonview import JsonFolderDocument


class JsonDirectoryDocument(JsonFolderDocument):

    def __call__(self):
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
        self.request.RESPONSE.setHeader('Content-Type',
                                        'application/json; charset=utf-8')
        feature_collection = geojson.FeatureCollection(json_result)
        feature_collection.update({'title': self.context.title})
        return geojson.dumps(feature_collection)
