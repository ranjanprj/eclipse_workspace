sap.ui.controller("com.slb.cus.controller.Master", {

/**
* Called when a controller is instantiated and its View controls (if available) are already created.
* Can be used to modify the View before it is displayed, to bind event handlers and do other one-time initialization.
* @memberOf Master
*/
	onInit: function() {
		
	},

/**
* Similar to onAfterRendering, but this hook is invoked before the controller's View is re-rendered
* (NOT before the first rendering! onInit() is used for that one!).
* @memberOf Master
*/
	onBeforeRendering: function() {

	},

/**
* Called when the View has been rendered (so its HTML is part of the document). Post-rendering manipulations of the HTML could be done here.
* This hook is the same one that SAPUI5 controls get after being rendered.
* @memberOf Master
*/
	onAfterRendering: function() {

	},

/**
* Called when the Controller is destroyed. Use this one to free resources and finalize activities.
* @memberOf Master
*/
	onExit: function() {

	},
	
	onPress: function (oEvent) {
		var oItem = oEvent.getSource();
		console.log(oItem.getBindingContext().getPath().substr(1));
		console.log(oItem.getBindingContext().getProperty("Vbeln"));
		var oRouter = sap.ui.core.UIComponent.getRouterFor(this);
//		oRouter.navTo("object", {
//			objectId: oItem.getBindingContext().getPath().substr(1)
//		});
//		
		oRouter.navTo("object", {
			objectId:   oItem.getBindingContext().getProperty("Vbeln")
		}, false);
	}

});