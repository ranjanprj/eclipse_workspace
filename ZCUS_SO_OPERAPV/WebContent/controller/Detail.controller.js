/*global location */
sap.ui.define([
	"com/slb/cus/operationalapproval/controller/BaseController",
	"sap/ui/model/json/JSONModel",
	"com/slb/cus/operationalapproval/model/formatter"
], function(BaseController, JSONModel, formatter) {
	"use strict";

	return BaseController.extend("com.slb.cus.operationalapproval.controller.Detail", {

		formatter: formatter,

		/* =========================================================== */
		/* lifecycle methods                                           */
		/* =========================================================== */

		onInit: function() {
			// Model used to manipulate control states. The chosen values make sure,
			// detail page is busy indication immediately so there is no break in
			// between the busy indication for loading the view's meta data
			var oViewModel = new JSONModel({
				busy: false,
				delay: 0,
				lineItemListTitle: this.getResourceBundle().getText("detailLineItemTableHeading")
			});

			this.getRouter().getRoute("object").attachPatternMatched(this._onObjectMatched, this);

			this.setModel(oViewModel, "detailView");

			this.getOwnerComponent().oWhenMetadataIsLoaded.then(this._onMetadataLoaded.bind(this));
		},

		/* =========================================================== */
		/* event handlers                                              */
		/* =========================================================== */

		/**
		 * Event handler when the share button has been clicked
		 * @param {sap.ui.base.Event} oEvent the butten press event
		 * @public
		 */
		onSharePress: function() {
			var oShareSheet = this.byId("shareSheet");
			oShareSheet.addStyleClass(this.getOwnerComponent().getContentDensityClass());
			oShareSheet.openBy(this.byId("shareButton"));
		},

		/**
		 * Event handler when the share by E-Mail button has been clicked
		 * @public
		 */
		onShareEmailPress: function() {
			var oViewModel = this.getModel("detailView");

			sap.m.URLHelper.triggerEmail(
				null,
				oViewModel.getProperty("/shareSendEmailSubject"),
				oViewModel.getProperty("/shareSendEmailMessage")
			);
		},

		/**
		 * Event handler when the share in JAM button has been clicked
		 * @public
		 */
		onShareInJamPress: function() {
			var oViewModel = this.getModel("detailView"),
				oShareDialog = sap.ui.getCore().createComponent({
					name: "sap.collaboration.components.fiori.sharing.dialog",
					settings: {
						object: {
							id: location.href,
							share: oViewModel.getProperty("/shareOnJamTitle")
						}
					}
				});

			oShareDialog.open();
		},

		/**
		 * Updates the item count within the line item table's header
		 * @param {object} oEvent an event containing the total number of items in the list
		 * @private
		 */
		onListUpdateFinished: function(oEvent) {
			var sTitle,
				iTotalItems = oEvent.getParameter("total"),
				oViewModel = this.getModel("detailView");

			// only update the counter if the length is final
			if (this.byId("lineItemsList").getBinding("items").isLengthFinal()) {
				if (iTotalItems) {
					sTitle = this.getResourceBundle().getText("detailLineItemTableHeadingCount", [iTotalItems]);
				} else {
					//Display 'Line Items' instead of 'Line items (0)'
					sTitle = this.getResourceBundle().getText("detailLineItemTableHeading");
				}
				oViewModel.setProperty("/lineItemListTitle", sTitle);
			}
		},

		/* =========================================================== */
		/* begin: internal methods                                     */
		/* =========================================================== */

		/**
		 * Binds the view to the object path and expands the aggregated line items.
		 * @function
		 * @param {sap.ui.base.Event} oEvent pattern match event in route 'object'
		 * @private
		 */
		_onObjectMatched: function(oEvent) {
			var sObjectId = oEvent.getParameter("arguments").objectId;
			this.getOwnerComponent().oWhenMetadataIsLoaded.then(function() {
				var sObjectPath = this.getModel().createKey("SalesOrderHeaderSet", {
					OrderNo: sObjectId
				});
				this._bindView("/" + sObjectPath);
			}.bind(this));
		},
		
		_setOrderNo: function(orderNo) {
			var urlHostName = window.location.hostname;
			var linkMap = {
				"localhost": "sape2d.dir.slb.com",
				"sapf2d.dir.slb.com": "sape2d.dir.slb.com",
				"sapf2q.dir.slb.com": "sape2q.dir.slb.com",
				"sapf2s.dir.slb.com": "sape2s.dir.slb.com",
				"sapf1p.dir.slb.com": "sape1q.dir.slb.com"
			};
			var link = "https://" + linkMap[urlHostName] + ":44310/sap/bc/gui/sap/its/webgui/?~transaction=VA03%20&VBAK-VBELN=" + orderNo +				"&~OKCODE=UER1";
			this.getView().byId("link_va03_app").setHref(link);
		},

		/**
		 * Binds the view to the object path. Makes sure that detail view displays
		 * a busy indicator while data for the corresponding element binding is loaded.
		 * @function
		 * @param {string} sObjectPath path to the object to be bound to the view.
		 * @private
		 */
		_bindView: function(sObjectPath) {
			// Set busy indicator during view binding
			var oViewModel = this.getModel("detailView");

			// If the view was not bound yet its not busy, only if the binding requests data it is set to busy again
			oViewModel.setProperty("/busy", false);

			this.getView().bindElement({
				path: sObjectPath,
				events: {
					change: this._onBindingChange.bind(this),
					dataRequested: function() {
						oViewModel.setProperty("/busy", true);
					},
					dataReceived: function() {
						oViewModel.setProperty("/busy", false);
					}
				}
			});
		},

		_onBindingChange: function() {
			var oView = this.getView(),
				oElementBinding = oView.getElementBinding();

			// No data for the binding
			if (!oElementBinding.getBoundContext()) {
				this.getRouter().getTargets().display("detailObjectNotFound");
				// if object could not be found, the selection in the master list
				// does not make sense anymore.
				this.getOwnerComponent().oListSelector.clearMasterListSelection();
				return;
			}

			var sPath = oElementBinding.getPath(),
				oResourceBundle = this.getResourceBundle(),
				oObject = oView.getModel().getObject(sPath),
				sObjectId = oObject.OrderNo,
				sObjectName = oObject.OrderNo,
				oViewModel = this.getModel("detailView");

			this.getOwnerComponent().oListSelector.selectAListItem(sPath);

			oViewModel.setProperty("/saveAsTileTitle", oResourceBundle.getText("shareSaveTileAppTitle", [sObjectName]));
			oViewModel.setProperty("/shareOnJamTitle", sObjectName);
			oViewModel.setProperty("/shareSendEmailSubject",
				oResourceBundle.getText("shareSendEmailObjectSubject", [sObjectId]));
			oViewModel.setProperty("/shareSendEmailMessage",
				oResourceBundle.getText("shareSendEmailObjectMessage", [sObjectName, sObjectId, location.href]));
			var orderNo = this.getView().getBindingContext().getProperty("OrderNo");
			this._setOrderNo(orderNo);
		},

		_onMetadataLoaded: function() {
			// Store original busy indicator delay for the detail view
			var iOriginalViewBusyDelay = this.getView().getBusyIndicatorDelay(),
				oViewModel = this.getModel("detailView"),
				oLineItemTable = this.byId("lineItemsList"),
				iOriginalLineItemTableBusyDelay = oLineItemTable.getBusyIndicatorDelay();

			// Make sure busy indicator is displayed immediately when
			// detail view is displayed for the first time
			oViewModel.setProperty("/delay", 0);
			oViewModel.setProperty("/lineItemTableDelay", 0);

			oLineItemTable.attachEventOnce("updateFinished", function() {
				// Restore original busy indicator delay for line item table
				oViewModel.setProperty("/lineItemTableDelay", iOriginalLineItemTableBusyDelay);
			});

			// Binding the view will set it to not busy - so the view is always busy if it is not bound
			oViewModel.setProperty("/busy", true);
			// Restore original busy indicator delay for the detail view
			oViewModel.setProperty("/delay", iOriginalViewBusyDelay);
		},
		
		onOperationalApproval : function(){
		    
		    var dialog = new sap.m.Dialog({
			      title: this.getResourceBundle().getText("approve"),
			      type: 'Message',
			      content: [
			        new sap.m.Text({ text: 'Are you sure you want to approve Sales Order?' }),
			        new sap.m.TextArea('approveDialogTextarea', {
			          width: '100%',
			          placeholder: 'Add note (optional)'
			        })
			      ],
			      beginButton: new sap.m.Button({
			        text: this.getResourceBundle().getText("approve"),
			        press: (function () {
			          var sText = sap.ui.getCore().byId('approveDialogTextarea').getValue();
			          var oModel = this.getView().getModel();
				  var payload = {};
				  payload.OrderNo = this.getView().getBindingContext().getProperty("OrderNo") ;
				  payload.Status = 'A';
				  payload.Comment = sText;
				  oModel.create("/SalesOrderUpdateSet", payload, null, { 
				      success : function(){
					  sap.m.MessageToast.show("Approved");
				  },
				  error : function(data){
				      sap.m.MessageToast.show("Error while approving:"+data);
				  }
				  })
			          dialog.close();
			        }).bind(this)
			      }),
			      endButton: new sap.m.Button({
			        text: 'Cancel',
			        press: function () {
			          dialog.close();
			        }
			      }),
			      afterClose: function() {
			        dialog.destroy();
			      }
			    });

			    dialog.open();
		   
		},
		
		onOperationalReject : function(){
		    
		    var dialog = new sap.m.Dialog({
			      title: this.getResourceBundle().getText("reject"),
			      type: 'Message',
			      content: [
			        new sap.m.Text({ text: 'Are you sure you want to reject Sales Order?' }),
			        new sap.m.TextArea('rejectDialogTextarea', {
			          width: '100%',
			          placeholder: 'Add note (optional)'
			        })
			      ],
			      beginButton: new sap.m.Button({
			        text: this.getResourceBundle().getText("reject"),
			        press: (function () {
			          var sText = sap.ui.getCore().byId('rejectDialogTextarea').getValue();
			          var oModel = this.getView().getModel();
				  var payload = {};
				  payload.OrderNo = this.getView().getBindingContext().getProperty("OrderNo") ;
				  payload.Status = 'R';
				  payload.Comment = sText;
				  oModel.create("/SalesOrderUpdateSet",payload,{ success : function(){
				      sap.m.MessageToast.show("Rejected");
				  },
				  error : function(data){
				      sap.m.MessageToast.show("Error while rejecting:"+data);
				  }
				  })
			          dialog.close();
			        }).bind(this)
			      }),
			      endButton: new sap.m.Button({
			        text: 'Cancel',
			        press: function () {
			          dialog.close();
			        }
			      }),
			      afterClose: function() {
			        dialog.destroy();
			      }
			    });

			    dialog.open();
		   
		},	

		
		onOperationalApproval : function(){
		    
		    var dialog = new sap.m.Dialog({
			      title: this.getResourceBundle().getText("approve"),
			      type: 'Message',
			      content: [
			        new sap.m.Text({ text: 'Are you sure you want to approve Sales Order?' }),
			        new sap.m.TextArea('approveDialogTextarea', {
			          width: '100%',
			          placeholder: 'Add note (optional)'
			        })
			      ],
			      beginButton: new sap.m.Button({
			        text: this.getResourceBundle().getText("approve"),
			        press: (function () {
			          var sText = sap.ui.getCore().byId('approveDialogTextarea').getValue();
			          var oModel = this.getView().getModel();
				  var payload = {};
				  payload.OrderNo = this.getView().getBindingContext().getProperty("OrderNo") ;
				  payload.Status = 'A';
				  payload.Comment = sText;
				  oModel.create("/SalesOrderUpdateSet", payload, null, { 
				      success : function(){
					  sap.m.MessageToast.show("Approved");
				  },
				  error : function(data){
				      sap.m.MessageToast.show("Error while approving:"+data);
				  }
				  })
			          dialog.close();
			        }).bind(this)
			      }),
			      endButton: new sap.m.Button({
			        text: 'Cancel',
			        press: function () {
			          dialog.close();
			        }
			      }),
			      afterClose: function() {
			        dialog.destroy();
			      }
			    });

			    dialog.open();
		   
		},
		
		onOperationalReject : function(){
		    
		    var dialog = new sap.m.Dialog({
			      title: this.getResourceBundle().getText("reject"),
			      type: 'Message',
			      content: [
			        new sap.m.Text({ text: 'Are you sure you want to reject Sales Order?' }),
			        new sap.m.TextArea('rejectDialogTextarea', {
			          width: '100%',
			          placeholder: 'Add note (optional)'
			        })
			      ],
			      beginButton: new sap.m.Button({
			        text: this.getResourceBundle().getText("reject"),
			        press: (function () {
			          var sText = sap.ui.getCore().byId('rejectDialogTextarea').getValue();
			          var oModel = this.getView().getModel();
				  var payload = {};
				  payload.OrderNo = this.getView().getBindingContext().getProperty("OrderNo") ;
				  payload.Status = 'R';
				  payload.Comment = sText;
				  oModel.create("/SalesOrderUpdateSet",payload,{ success : function(){
				      sap.m.MessageToast.show("Rejected");
				  },
				  error : function(data){
				      sap.m.MessageToast.show("Error while rejecting:"+data);
				  }
				  })
			          dialog.close();
			        }).bind(this)
			      }),
			      endButton: new sap.m.Button({
			        text: 'Cancel',
			        press: function () {
			          dialog.close();
			        }
			      }),
			      afterClose: function() {
			        dialog.destroy();
			      }
			    });

			    dialog.open();
		   
		}

	});

		

	});
	
	

});