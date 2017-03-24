sap.ui.define([
	"sap/ui/core/UIComponent",
	"sap/ui/Device",
	"sap/ui/model/odata/ODataModel"
	
	
], function(UIComponent, Device, ODataModel) {
	"use strict";

	return UIComponent.extend("com.slb.cus.Component", {

		metadata: {
			"version": "1.0.0",
			"rootView": {
				viewName: "com.slb.cus.view.App",
				type: sap.ui.core.mvc.ViewType.XML
			},
			"dependencies": {
				"libs": ["sap.ui.core", "sap.m", "sap.ui.layout"]
			},
			"config": {
				"i18nBundle": "com.slb.cus.i18n.i18n",
				"serviceUrl": "proxy/https/sapf2d.dir.slb.com:44310/sap/opu/odata/SAP/ZCUS_TEST_SALES_ORDER_SRV/",
				"icon": "",
				"favIcon": "",
				"phone": "",
				"phone@2": "",
				"tablet": "",
				"tablet@2": ""
			},
			"routing" : {
				"config": {
					"routerClass" : "sap.m.routing.Router",
					"viewType" : "XML",
					"viewPath" : "com.slb.cus.view",
					"controlId" : "splitApp",
					"controlAggregation" : "detailPages"
				},
				"routes": [{
					"pattern": "",
					"name": "master",
					"target": ["object","master"]
				}, {
					"pattern": "object/{objectId}",
					"name": "object",
					"target": ["master", "object"]
				}],

				"targets": {
					"master": {
						"viewName": "Master",
						"viewLevel": 1,
						"viewId": "master",
						"controlAggregation": "masterPages"
					},
					"object": {
						"viewName": "Detail",
						"viewId": "detail",
						"viewLevel": 2
					}
				}
			}
		},

		/**
		 * The component is initialized by UI5 automatically during the startup of the app and calls the init method once.
		 * In this method, the resource and application models are set.
		 * @public
		 * @override
		 */
		init: function() {
			var mConfig = this.getMetadata().getConfig();
			UIComponent.prototype.init.apply(this, arguments);
			// create the views based on the url/hash

			var serviceURL = mConfig.serviceUrl;
			
			var oModel = new ODataModel(serviceURL,false);
			
			this.setModel(oModel);
	
			
			
			this.getRouter().initialize();
			
			
		},
		
		
	});
});