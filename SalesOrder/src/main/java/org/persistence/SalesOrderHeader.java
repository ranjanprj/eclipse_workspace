package org.persistence;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

import javax.persistence.*;

/**
 * Entity implementation class for Entity: SalesOrderHeader
 *
 */
@Entity

public class SalesOrderHeader implements Serializable {

	
	private static final long serialVersionUID = 1L;
	@Id
	@GeneratedValue(strategy= GenerationType.AUTO)

	private long id;
	private String salesOrderNumber;
	private double salesOrderTotal;
	@Temporal(TemporalType.TIMESTAMP)
	private Date salesOrderDate;
	
	@OneToMany(cascade=CascadeType.ALL)
	List<SalesOrderHeaderItem> salesOrderItems;
	
	public SalesOrderHeader() {
		super();
	
	}

	public long getId() {
		return id;
	}

	public void setId(long id) {
		this.id = id;
	}

	public String getSalesOrderNumber() {
		return salesOrderNumber;
	}

	public void setSalesOrderNumber(String salesOrderNumber) {
		this.salesOrderNumber = salesOrderNumber;
	}

	public double getSalesOrderTotal() {
		return salesOrderTotal;
	}

	public void setSalesOrderTotal(double salesOrderTotal) {
		this.salesOrderTotal = salesOrderTotal;
	}

	public Date getSalesOrderDate() {
		return salesOrderDate;
	}

	public void setSalesOrderDate(Date salesOrderDate) {
		this.salesOrderDate = salesOrderDate;
	}

	public List<SalesOrderHeaderItem> getSalesOrderItems() {
		return salesOrderItems;
	}

	public void setSalesOrderItems(List<SalesOrderHeaderItem> salesOrderItems) {
		this.salesOrderItems = salesOrderItems;
	}
	
	public void addSalesOrderItems(SalesOrderHeaderItem salesOrderItems) {
		if(this.getSalesOrderItems() == null ){
			this.setSalesOrderItems(new ArrayList<SalesOrderHeaderItem>());
		}
		
		this.getSalesOrderItems().add(salesOrderItems);
	}
	
   
}
