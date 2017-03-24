package org.persistence;

import java.io.Serializable;
import java.util.List;

import javax.persistence.*;

/**
 * Entity implementation class for Entity: OrganizationData
 *
 */
@Entity
@Table(name = "OrganizationData")
public class OrganizationData implements Serializable {

	
	private static final long serialVersionUID = 1L;
	@Id
	@GeneratedValue(strategy= GenerationType.AUTO)

	private long id;
	private String salesOrganization,distributionChannel,division;
	
	@OneToMany
	private List<SalesOrder> salesOrder;
	public OrganizationData() {
		super();
	}
	public long getId() {
		return id;
	}
	public void setId(long id) {
		this.id = id;
	}
	public String getSalesOrganization() {
		return salesOrganization;
	}
	public void setSalesOrganization(String salesOrganization) {
		this.salesOrganization = salesOrganization;
	}
	public String getDistributionChannel() {
		return distributionChannel;
	}
	public void setDistributionChannel(String distributionChannel) {
		this.distributionChannel = distributionChannel;
	}
	public String getDivision() {
		return division;
	}
	public void setDivision(String division) {
		this.division = division;
	}
	public List<SalesOrder> getSalesOrder() {
		return salesOrder;
	}
	public void setSalesOrder(List<SalesOrder> salesOrder) {
		this.salesOrder = salesOrder;
	}
	
	
   
}
