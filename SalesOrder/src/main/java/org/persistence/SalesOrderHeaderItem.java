package org.persistence;

import java.io.Serializable;
import javax.persistence.*;

/**
 * Entity implementation class for Entity: SalesOrderHeaderItem
 *
 */
@Entity
public class SalesOrderHeaderItem implements Serializable {

	
	private static final long serialVersionUID = 1L;
	@Id
	@GeneratedValue(strategy= GenerationType.AUTO)

	private long id;
	
	private String itemName;
	private String itemNumber;
	private String itemQuantity;
	private String itemUOM;
	private double itemCost;

	public SalesOrderHeaderItem() {
		super();
	}

	public String getItemName() {
		return itemName;
	}

	public void setItemName(String itemName) {
		this.itemName = itemName;
	}

	public String getItemNumber() {
		return itemNumber;
	}

	public void setItemNumber(String itemNumber) {
		this.itemNumber = itemNumber;
	}

	public String getItemQuantity() {
		return itemQuantity;
	}

	public void setItemQuantity(String itemQuantity) {
		this.itemQuantity = itemQuantity;
	}

	public String getItemUOM() {
		return itemUOM;
	}

	public void setItemUOM(String itemUOM) {
		this.itemUOM = itemUOM;
	}

	public double getItemCost() {
		return itemCost;
	}

	public void setItemCost(double itemCost) {
		this.itemCost = itemCost;
	}
   
	
}
