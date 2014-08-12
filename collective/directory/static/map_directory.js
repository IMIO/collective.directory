/*categories = [
    {
        "name":"Mes assos",
        "contents": [{
            "name": "assos 1",
            "url": "http://localhost:8080/Plone/directories/assosiations/divers/@@geo-json.json"
        }],
    }, {
        "name": "Sports",
        "contents": [{
            "name": "foot",
            "url": "http://localhost:8080/Plone/directories/sports/football/@@geo-json.json"
        }, {
            "name": "hockey",
            "url": "http://localhost:8080/Plone/directories/sports/hockey/@@geo-json.json"
        }]
    }
]*/

categories = $('#geojson_urls').data('geojson_urls');
controldirectory = L.control.directory(categories).addTo(map);
/*
for (var i=0; i < categories.length; i++) {
    for (var j=0; j < categories[i].urls.length; j++) {
        url = categories[i].urls[j];
        $.getJSON(url, function(data) {
            layername = data.title;
            geojson = L.geoJson(data, {
                onEachFeature: function (feature, layer) {
                    layer.bindPopup(
                        '<a href="'+feature.properties.url+'" target="_blank">'+
                        '<h3>'+feature.properties.title+'</h3>'+
                        '</a>'+
                        '<p>'+feature.properties.description+'</p>');
                },
                pointToLayer: function (feature, latlng) {
                    var CustomIcon = L.Icon.Default.extend({
                        options: {
                            iconUrl: feature.style.image
                        }
                     });
                    var customIcon = new CustomIcon();
                    return L.marker(latlng, {icon: customIcon});
                }
            }).addTo(map);
            controldirectory.addOverlay(geojson, layername);
        });
    }
}
*/
