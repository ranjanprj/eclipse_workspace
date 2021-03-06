/*global location */
sap.ui.define([
	"com/slb/cus/billingapproval/controller/BaseController",
	"sap/ui/model/json/JSONModel",
	"com/slb/cus/billingapproval/model/formatter",
	"sap/m/MessageBox"
], function(BaseController, JSONModel, formatter) {
	"use strict";
	return BaseController.extend("com.slb.cus.billingapproval.controller.Detail", {
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
		onAfterRendering: function() {

		},
		/* =========================================================== */
		/* event handlers                                              */
		/* =========================================================== */

		/**
		 * Updates the item count within the line item table's header
		 * @param {object} oEvent an event containing the total number of items in the list
		 * @private
		 */
		onListUpdateFinished: function(oEvent) {
			var sTitle, iTotalItems = oEvent.getParameter("total"),
				oViewModel = this.getModel("detailView");
			// only update the counter if the length is final
			if (this.byId("lineItemsList").getBinding("items").isLengthFinal()) {
				if (iTotalItems) {
					sTitle = this.getResourceBundle().getText("detailLineItemTableHeadingCount", [iTotalItems]);
				} else {
					//Display 'Line Items' instead of 'Line items (0)'
					sTitle = this.getResourceBundle().getText("detailLineItemTableHeading");
				}
				oViewModel.setProperty("/lineItemListTitle", iTotalItems);
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
		// This mapping is for switching the server when the Gateway server changes
		_setOrderNo: function(orderNo) {
			var urlHostName = window.location.hostname;
			var linkMap = {
				"localhost": "sape2d.dir.slb.com",
				"sapf2d.dir.slb.com": "sape2d.dir.slb.com",
				"sapf2q.dir.slb.com": "sape2q.dir.slb.com",
				"sapf2s.dir.slb.com": "sape2s.dir.slb.com",
				"sapf1p.dir.slb.com": "sape1q.dir.slb.com"
			};
			var link = "https://" + linkMap[urlHostName] + ":44310/sap/bc/gui/sap/its/webgui/?~transaction=VA03%20&VBAK-VBELN=" + orderNo +
				"&~OKCODE=UER1";
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
			oViewModel.setProperty("/shareSendEmailSubject", oResourceBundle.getText("shareSendEmailObjectSubject", [sObjectId]));
			oViewModel.setProperty("/shareSendEmailMessage", oResourceBundle.getText("shareSendEmailObjectMessage", [
				sObjectName,
				sObjectId,
				location.href
			]));
			//TODO
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
		/**
		 *@memberOf com.slb.cus.billingapproval.controller.Detail
		 */

		openApproveDialog: function(evt) {
			var orderNo = this.getView().getBindingContext().getProperty("OrderNo");
			this._oApprovalButton = evt.getSource().getText();
			// Populate JSON Model
			this._getSalesOrderUpdateData(orderNo);
			this._getSalesOrderUpdateUsrStatusData(orderNo);

		},

		_openApprovalDialogAfterRead: function() {
			var soModel = this.getModel("SalesOrderUpdateModel");
			var soStatusModel = this.getModel("SalesOrderUpdateUsrStatusModel");
			if (!this._oViewSettingsDialog) {
				this._oViewSettingsDialog = sap.ui.xmlfragment("com.slb.cus.billingapproval.view.BillingApprovalDialog", this);
				this.getView().addDependent(this._oViewSettingsDialog);
				// forward compact/cozy style into Dialog
				this._oViewSettingsDialog.addStyleClass(this.getOwnerComponent().getContentDensityClass());
			}

			this._oViewSettingsDialog.setModel(soModel, "SalesOrderUpdateModel");
			this._oViewSettingsDialog.setModel(soStatusModel, "SalesOrderUpdateUsrStatusModel");

			this._oViewSettingsDialog.open();
		},
		_getSalesOrderUpdateData: function(orderNo) {

			var oModel = this.getView().getModel();
			// var oView = this.getView();
			var that = this;
			oModel.read("/SalesOrderUpdateSet('" + orderNo + "')", {
				success: function(oData, oResponse) {
					var soupdateJSON = new sap.ui.model.json.JSONModel();
					soupdateJSON.setData(oData);
					// oView.setModel(soupdateJSON, "SalesOrderUpdateModel");
					that.setModel(soupdateJSON, "SalesOrderUpdateModel");

				},
				error: function(data) {
					sap.m.MessageToast.show("Error while fetching data:" + data);
				}
			});

		},
		_getSalesOrderUpdateUsrStatusData: function(orderNo) {

			var oModel = this.getView().getModel();
			// var oView = this.getView();
			var that = this;
			var approvalButtonType = this._oApprovalButton;

			oModel.read("/SalesOrderUpdateSet('" + orderNo + "')/SalesOrderUpdate_USR_STSet", {
				success: function(oData, oResponse) {
					var soupdateJSON = new sap.ui.model.json.JSONModel();

					oData.results.map(function(elem) {
						if (elem.Active === "false") {
							elem.Active = false;
						} else {
							elem.Active = true;
						}

						if (approvalButtonType && approvalButtonType === "Approve") {
							// Inital status default unchecked
							if (elem.Status === "Z001") {
								elem.Active = false;
								elem.CheckBoxEnabled = true;
							}
							// Released to Billing default checked but editable.
							if (elem.Status === "Z010") {
								elem.Active = true;
								elem.CheckBoxEnabled = true;
							}
							// Cancelled default uncheck not editable
							if (elem.Status === "Z012") {
								elem.Active = false;
								elem.CheckBoxEnabled = false;
							}
							// Rev Recog default not editable
							if (elem.Status === "Z011") {
								// elem.Active = true;
								elem.CheckBoxEnabled = false;
							}
						} else if (approvalButtonType && approvalButtonType === "Put on Hold") {
							// Released to Billing default unchecked but uneditable.
							if (elem.Status === "Z010") {
								elem.Active = false;
								elem.CheckBoxEnabled = false;
							}
							// Inital status default checked
							if (elem.Status === "Z001") {
								elem.Active = true;
								// elem.CheckBoxEnabled = false;
							}
							// Cancelled default uncheck not editable
							if (elem.Status === "Z012") {
								elem.Active = false;
								elem.CheckBoxEnabled = false;
							}
						}
					});

					soupdateJSON.setData(oData);

					that.setModel(soupdateJSON, "SalesOrderUpdateUsrStatusModel");
					that._openApprovalDialogAfterRead();

				},
				error: function(data) {
					sap.m.MessageToast.show("Error while reading:" + data);
				}
			});

		},
		onBillingApprovalDialogSubmit: function() {

			//sap.ui.core.Fragment.byId("myFrag", "myControl")

			var soUpdateModel = this._oViewSettingsDialog.getModel("SalesOrderUpdateModel");
			var soupdateUsrStatusModel = this._oViewSettingsDialog.getModel("SalesOrderUpdateUsrStatusModel");

			var oModel = this.getView().getModel();
			var payload = {};
			payload.OrderNo = this.getView().getBindingContext().getProperty("OrderNo");
			payload.Comment = soUpdateModel.getData().Comment;
			if (this._oApprovalButton === "Approve") {
				payload.Status = "A";
			} else if (this._oApprovalButton === "Put on Hold") {
				payload.Status = "R";
				// if (payload.Comment === "" || payload.Comment.trim().length === 0) {

				// 	sap.m.MessageToast.show("Please provide comments for rejection.");
				// 	return;
				// }
			}

			var usrStatusJson = JSON.stringify(this.transformUsrStatusPayload(soupdateUsrStatusModel));
			payload.UsrStatus = usrStatusJson;
			// console.log(soupdateUsrStatusModel);
			// console.log(usrStatusJson);
			var that = this;
			var successMsg = payload.Status === "A" ? "Sales Order Approved" : "Sales Order Put on Hold";
			
			oModel.create("/SalesOrderUpdateSet", payload, {
				success: function() {
					sap.m.MessageToast.show(successMsg);
					that._oViewSettingsDialog.close();
					try{
						oModel.refresh();
					}catch(ex){
						console.log("Error while refreshing component model",ex);
					}

				},
				error: function(data) {
//					sap.m.MessageToast.show("Error processing Sales Order");
					that._oViewSettingsDialog.close();

				}
			});

		},
		onBillingApprovalDialogClose: function() {

			this._oViewSettingsDialog.close();
		},

		afterClose: function() {
			this._oViewSettingsDialog.destroy(true);
			this._oViewSettingsDialog = undefined;
		},

		onCheckBoxSelect: function(elem) {

		},
		transformUsrStatusPayload: function(soupdateUsrStatusModel) {
			var SalesOrderUpdate_USR_STSet = [];
			var data = soupdateUsrStatusModel.getData().results;
			for (var i in data) {
				SalesOrderUpdate_USR_STSet.push({
					"ORDER_NO": data[i].ORDER_NO,
					"USR_STAT": data[i].USR_STAT,
					"Objnr": data[i].Objnr,
					"Status": data[i].Status,
					"StatusTxt": data[i].StatusTxt,
					"Active": data[i].Active

				});

			}
			return SalesOrderUpdate_USR_STSet;
		}
	});
});