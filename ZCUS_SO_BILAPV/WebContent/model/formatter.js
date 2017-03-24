sap.ui.define([], function() {
	"use strict";

	return {
		/**
		 * Rounds the currency value to 2 digits
		 * @public
		 * @param {string} sValue value to be formatted
		 * @returns {string} formatted currency value with 2 digits
		 */
		currencyValue: function(sValue) {
			if (!sValue) {
				return "";
			}

			return parseFloat(sValue).toFixed(2);
		},

		/**
		 * Returns a configuration object for the {@link sap.ushell.ui.footerbar.AddBookMarkButton} "appData" property
		 * @public
		 * @param {string} sTitle the title for the "save as tile" dialog
		 * @returns {object} the configuration object
		 */
		shareTileData: function(sTitle) {
			return {
				title: sTitle
			};
		},

		statusState: function(value) {
			var map = {
				"Not yet processed": "Warning",
				"Partially processed": "Success",
				"Completely processed": "Success"
			};
			return (value && map[value]) ? map[value] : "None";
		},
		
		checkBoxTruthy: function(value) {
			var map = {
				"true": true,
				"false" : false
			};
			return (value && map[value]) ? map[value] : false;
		},

		date: function(value) {
			if (value) {
				var oDateFormat = sap.ui.core.format.DateFormat.getDateTimeInstance({

					pattern: "MMMM dd, yyyy"
				});
				return oDateFormat.format(new Date(value));
			} else {
				return value;
			}
		}
	};

});