L.Control.Directory = L.Control.extend({
    options: {
        collapsed: true,
        position: 'topright',
        autoZIndex: true
    },

    initialize: function (geojsonlayers, options) {
        L.setOptions(this, options);

        this._layers = {};
        this._layersList = {};
        this._lastZIndex = 0;
        this._handlingClick = false;
        this.jsonDirectories = geojsonlayers.length;
        this._createGeoJsonLayer(geojsonlayers);
        this.geojsonlayers = geojsonlayers;
        //this._updateGeoJsonLayer();
    },

    _createGeoJsonLayer: function(geojsonlayers) {
        for (var i=0; i < geojsonlayers.length; i++) {
            for (var j=0; j < geojsonlayers[i].contents.length; j++) {
                geojson = L.geoJson('', {
                    onEachFeature: onEachFeature,
                    pointToLayer: pointToLayer,
                });
                url = geojsonlayers[i].contents[j].url;
                name = geojsonlayers[i].contents[j].name;
                this._addLayer(geojson, name, true, i, url);
            }
        }
    },

    _updateGeoJsonLayer: function() {
        var layer;
        for (var key in this._layers) {
            layer = this._layers[key];
            var url = layer.url;
            $.getJSON(url, function(data) {
                layer.name = data.title;
                layer.addData(data);
                layer.addTo(this._map);
            });
        }
    },

    onAdd: function () {
        this._initLayout();
        this._update();

        return this._container;
    },

    removeLayer: function (layer) {
        layer.off('add remove', this._onLayerChange, this);

        delete this._layers[L.stamp(layer)];
        return this._update();
    },

    _initLayout: function () {
        var className = 'leaflet-control-layers',
            container = this._container = L.DomUtil.create('div', className);

        // makes this work on IE touch devices by stopping it from firing a mouseout event when the touch is released
        container.setAttribute('aria-haspopup', true);

        L.DomEvent.on(container, 'click', L.DomEvent.stopPropagation);

        var form = this._form = L.DomUtil.create('form', className + '-list');

        L.DomUtil.addClass(this._container, 'leaflet-control-layers-expanded');

        for (var i=0; i < this.jsonDirectories; i++) {
            name = this.geojsonlayers[i].name;
            h2 = L.DomUtil.create('h3', 'category-title', form);
            h2.innerHTML = name;
            this._layersList[i] = h2;
            this._layersList[i] = L.DomUtil.create('div', className + '-overlays', form);
            if (i < this.jsonDirectories-1){
                this._separator = L.DomUtil.create('div', className + '-separator', form);
            }
        }
        //this._geojsonlayersList = L.DomUtil.create('div', className + '-overlays', form);

        container.appendChild(form);
    },

    _addLayer: function (layer, name, overlay, container, url) {
        layer.on('add remove', this._onLayerChange, this);

        var id = L.stamp(layer);
        var layername;
        var self=this;
        var layer = layer;
        $.getJSON(url, function(data) {
            layer.addData(data);
        });

        self._layers[id] = {
            layer: layer,
            name: name,
            overlay: true,
            container: container,
            url: url
        };
        layer.addTo(map);

        if (this.options.autoZIndex && layer.setZIndex) {
            this._lastZIndex++;
            layer.setZIndex(this._lastZIndex);
        }
    },

    _update: function () {
        if (!this._container) { return; }

        for (var i=0; i < this.jsonDirectories; i++) {
            //L.DomUtil.empty(this._layersList[i]);
        }

        var i, obj;

        for (i in this._layers) {
            obj = this._layers[i];
            this._addItem(obj);
        }

        return this;
    },

    _onLayerChange: function (e) {
        if (!this._handlingClick) {
            this._update();
        }

        var overlay = this._layers[L.stamp(e.target)].overlay;

        var type = overlay ?
            (e.type === 'add' ? 'overlayadd' : 'overlayremove') :
            (e.type === 'add' ? 'baselayerchange' : null);

        if (type) {
            this._map.fire(type, e.target);
        }
    },


    _addItem: function (obj) {
        var label = document.createElement('label'),
            checked = this._map.hasLayer(obj.layer),
            input;

        input = document.createElement('input');
        input.type = 'checkbox';
        input.className = 'leaflet-control-layers-selector';
        input.defaultChecked = checked;

        input.layerId = L.stamp(obj.layer);

        L.DomEvent.on(input, 'click', this._onInputClick, this);

        var name = document.createElement('span');
        name.innerHTML = ' ' + obj.name;

        label.appendChild(input);
        label.appendChild(name);

        var container = this._layersList[obj.container]

        container.appendChild(label);

        return label;
    },

    _onInputClick: function () {
        var inputs = this._form.getElementsByTagName('input'),
            input, layer, hasLayer;

        this._handlingClick = true;

        for (var i = 0, len = inputs.length; i < len; i++) {
            input = inputs[i];
            layer = this._layers[input.layerId].layer;
            hasLayer = this._map.hasLayer(layer);

            if (input.checked && !hasLayer) {
                this._map.addLayer(layer);

            } else if (!input.checked && hasLayer) {
                this._map.removeLayer(layer);
            }
        }

        this._handlingClick = false;

        //this._refocusOnMap();
    },

});


L.control.directory = function (geojsonlayers, options) {
    return new L.Control.Directory(geojsonlayers, options);
};

function onEachFeature(feature, layer) {
    layer.bindPopup(
            '<a href="'+feature.properties.url+'" target="_blank">'+
            '<h3>'+feature.properties.title+'</h3>'+
            '</a>'+
            '<p>'+feature.properties.description+'</p>');
    layer.on('mouseover', function (e) {
        this.openPopup();
    });

    layer.on('mouseout', function (e) {
        this.closePopup()
    });
}

function pointToLayer (feature, latlng) {
    var CustomIcon = L.Icon.Default.extend({
        options: {
            iconUrl: feature.style.image
        }
    });
    var customIcon = new CustomIcon();
    return L.marker(latlng, {icon: customIcon});
}

