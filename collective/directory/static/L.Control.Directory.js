L.Control.Directory = L.Control.Layers.extend({
    options: {
        collapsed: false,
        position: 'topleft',
        autoZIndex: true
    },
    initialize: function (overlays, directory_title, options) {
        L.setOptions(this, options);

        this._layers = {};
        this._lastZIndex = 0;
        this._handlingClick = false;
        this._directory_title = directory_title;
        this.selectalltext = "Tout sélectionner";
        this.unselectalltext = "Tout désélectionner";
        //this._markers = markers;
        for (i in overlays) {
            this._addLayer(overlays[i], i, true);
        }
    },

    _initLayout: function () {
        var className = 'leaflet-control-layers',
            container = this._container = L.DomUtil.create('div', className);

        //Makes this work on IE10 Touch devices by stopping it from firing a mouseout event when the touch is released
        container.setAttribute('aria-haspopup', true);

        if (!L.Browser.touch) {
            L.DomEvent
                .disableClickPropagation(container)
                .disableScrollPropagation(container);
        } else {
            L.DomEvent.on(container, 'click', L.DomEvent.stopPropagation);
        }

        var form = this._form = L.DomUtil.create('form', className + '-list');

        if (this.options.collapsed) {
            if (!L.Browser.android) {
                L.DomEvent
                    .on(container, 'mouseover', this._expand, this)
                    .on(container, 'mouseout', this._collapse, this);
            }
            var link = this._layersLink = L.DomUtil.create('a', className + '-toggle', container);
            link.href = '#';
            link.title = 'Layers';

            if (L.Browser.touch) {
                L.DomEvent
                    .on(link, 'click', L.DomEvent.stop)
                    .on(link, 'click', this._expand, this);
            }
            else {
                L.DomEvent.on(link, 'focus', this._expand, this);
            }
            //Work around for Firefox android issue https://github.com/Leaflet/Leaflet/issues/2033
            L.DomEvent.on(form, 'click', function () {
                setTimeout(L.bind(this._onInputClick, this), 0);
            }, this);

            this._map.on('click', this._collapse, this);
            // TODO keyboard accessibility
        } else {
            this._expand();
        }

        this._baseLayersList = L.DomUtil.create('div', className + '-base', form);
        this._separator = L.DomUtil.create('div', className + '-separator', form);

        var selectall = this._selectall = L.DomUtil.create('a', 'category-title', form);
        selectall.innerHTML = this.unselectalltext;
        this.isselectall = false;
        L.DomEvent.on(selectall, 'click', this._selectAll, this);
        var h3 = L.DomUtil.create('h3', 'category-title', form);
        h3.innerHTML = this._directory_title;
        h3.setAttribute('rel', className + '-overlays');
        this._overlaysList = h3;
        L.DomEvent.addListener(h3, 'click', this._toggleTitle, this);
        this._overlaysList = L.DomUtil.create('div', className + '-overlays', form);

        container.appendChild(form);
    },
    _update: function () {
        if (!this._container) {
            return;
        }

        this._baseLayersList.innerHTML = '';
        this._overlaysList.innerHTML = '';

        var baseLayersPresent = false,
            overlaysPresent = false,
            i, obj;

        for (i in this._layers) {
            obj = this._layers[i];
            this._addItem(obj);
            overlaysPresent = overlaysPresent || obj.overlay;
            baseLayersPresent = baseLayersPresent || !obj.overlay;
        }

        this._separator.style.display = overlaysPresent && baseLayersPresent ? '' : 'none';
    },
    _onLayerChange: function (e) {
        var obj = this._layers[L.stamp(e.layer)];

        if (!obj) { return; }

        if (!this._handlingClick) {
            this._update();
        }

        var type = obj.overlay ?
            (e.type === 'layeradd' ? 'overlayadd' : 'overlayremove') :
            (e.type === 'layeradd' ? 'baselayerchange' : null);

        if (type) {
            this._map.fire(type, obj);
        }
    },/*
    _addItem: function (obj) {
        var label = document.createElement('label'),
            input;
        for (var l in obj.layer._layers){
            var checked = this._markers.hasLayer(obj.layer._layers[l]);
        }

        if (obj.overlay) {
            input = document.createElement('input');
            input.type = 'checkbox';
            input.className = 'leaflet-control-layers-selector';
            input.defaultChecked = checked;
        } else {
            input = this._createRadioElement('leaflet-base-layers', checked);
        }

        input.layerId = L.stamp(obj.layer);

        L.DomEvent.on(input, 'click', this._onInputClick, this);

        var name = document.createElement('span');
        name.innerHTML = ' ' + obj.name;

        label.appendChild(input);
        label.appendChild(name);

        var container = obj.overlay ? this._overlaysList : this._baseLayersList;
        container.appendChild(label);

        return label;
    },*/
    /*_initLayout: function () {
        var className = 'leaflet-control-layers',
            container = this._container = L.DomUtil.create('div', className);

        // makes this work on IE touch devices by stopping it from firing a mouseout event when the touch is released
        container.setAttribute('aria-haspopup', true);

        if (!L.Browser.touch) {
            L.DomEvent
                .disableClickPropagation(container);
                //.disableScrollPropagation(container);
        } else {
            L.DomEvent.on(container, 'click', L.DomEvent.stopPropagation);
        }

        var form = this._form = L.DomUtil.create('form', className + '-list');

        L.DomUtil.addClass(this._container, 'leaflet-control-layers-expanded');

        var selectall = this._selectall = L.DomUtil.create('a', 'category-title', form);
        selectall.innerHTML = this.unselectalltext;
        this.isselectall = false;
        L.DomEvent.on(selectall, 'click', this._selectAll, this);

        i=0;
        name = this._directory_title


        var h3 = L.DomUtil.create('h3', 'category-title-'+i, form);
        h3.innerHTML = name;
        h3.setAttribute('rel', className + '-overlays-'+i);
        this._layersList = h3;
        L.DomEvent.addListener(h3, 'click', this._toggleTitle, this);
        this._layersList = L.DomUtil.create('div', className + '-overlays-'+i, form);


        //this._geojsonlayersList = L.DomUtil.create('div', className + '-overlays', form);

        container.appendChild(form);
    },*/

    _selectAll: function() {
        var inputs = this._form.getElementsByTagName('input'),
            input, layer, hasLayer;

        this._handlingClick = true;

        for (var i = 0, len = inputs.length; i < len; i++) {
            input = inputs[i];
            layer = this._layers[input.layerId].layer;
            hasLayer = this._map.hasLayer(layer);

            if (this.isselectall) {
                //markers.addLayers(layer)
                this._map.addLayer(layer);
                input.checked = true;
            }else if (!this.isselectall) {
                //markers.removeLayers(layer);
                this._map.removeLayer(layer);
                input.checked = false;
            }
        }
        if (this.isselectall) {
            this._selectall.innerHTML = this.unselectalltext;
            this.isselectall = false;
        } else if (!this.isselectall) {
            this._selectall.innerHTML = this.selectalltext;
            this.isselectall = true;
        }
        this._handlingClick = false;
    },

    _toggleTitle:  function(e) {
        $('.'+e.currentTarget.getAttribute('rel')).toggle(200);
    }
});

L.control.directory = function (geojsonlayers, directory_title, options) {
    return new L.Control.Directory(geojsonlayers, directory_title, options);
};
