url = $('#geojsons_url').data('geojsons_url');
directory_title = $('#directory_title').data('directory_title');


//var geojson =  {};
/*$.getJSON(url, function(data) {
    var geojsons = data;
    for (var g in geojsons) {
        geojson_data = geojsons[g];
        name = geojson_data.title;
        geojson[name] = L.geoJson(geojson_data, {
            onEachFeature: onEachFeature,
            pointToLayer: pointToLayer
        });
        markers.addLayer(geojson[name]).addTo(map);
        //map.addLayer(markers);
    }
    //map.addLayer(markers);
    var lcontrol = L.control.layers(null, geojson, {collapsed:false, position: 'topleft'});
    map.addControl(lcontrol);
});*/

//map.addLayer(markers);
//emptyLayers = L.layerGroup([]);
var lcontrol = L.control.directory(geojsons, directory_title);
map.addControl(lcontrol);