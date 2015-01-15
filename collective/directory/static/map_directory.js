url = $('#geojsons_url').data('geojsons_url');
directory_title = $('#directory_title').data('directory_title');

var categories_meta = {},
    overlayMaps = {},
    markers_category = {},
    leaflet_meta = {};

for(var index in geojsons) {
    markers_category[index] = [];
    overlayMaps[index] = geojsons[index];
}

for(var index in geojsons) {
    markers.addLayer(geojsons[index]);
    geojsons[index].addData(data[index])
    markers_category[index].push(geojsons[index]);
}

var control = L.control.directory(geojsons, directory_title);
/*var control = L.control.layers(null, overlayMaps, {
        collapsed: false,
        position: 'topleft'
    }
);*/

map.addControl(control);
/*map.addLayer(markers);

for (var row in control._layers) {
    leaflet_meta[L.Util.stamp(control._layers[row].layer)] = control._layers[row].name;
}

for (var row in control._layers) {
    leaflet_meta[L.Util.stamp(control._layers[row].layer)] = control._layers[row].name;
}
map.on('overlayadd', function (a) {
    var category_index = leaflet_meta[L.Util.stamp(a.layer)];
    markers.addLayers(markers_category[category_index]);
});
map.on('overlayremove', function (a) {
    var category_index = leaflet_meta[L.Util.stamp(a.layer)];
    markers.removeLayers(markers_category[category_index]);
});*/
