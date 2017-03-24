package org.persistence;

import java.io.Serializable;
import java.util.List;

import javax.persistence.*;

/**
 * Entity implementation class for Entity: SLBOrganization
 *
 */
@Entity
@Table(name = "OrganizationData")
public class SLBOrganization implements Serializable {

	@Id
	@GeneratedValue(strategy= GenerationType.AUTO)

	private long id;
	private static final long serialVersionUID = 1L;

	private String area,geo,subGeo,segment,subSegment;
	@OneToMany
	private List<SalesOrder> salesOrder;
	public SLBOrganization() {
		super();
	}
	public long getId() {
		return id;
	}
	public void setId(long id) {
		this.id = id;
	}
	public String getArea() {
		return area;
	}
	public void setArea(String area) {
		this.area = area;
	}
	public String getGeo() {
		return geo;
	}
	public void setGeo(String geo) {
		this.geo = geo;
	}
	public String getSubGeo() {
		return subGeo;
	}
	public void setSubGeo(String subGeo) {
		this.subGeo = subGeo;
	}
	public String getSegment() {
		return segment;
	}
	public void setSegment(String segment) {
		this.segment = segment;
	}
	public String getSubSegment() {
		return subSegment;
	}
	public void setSubSegment(String subSegment) {
		this.subSegment = subSegment;
	}
	public List<SalesOrder> getSalesOrder() {
		return salesOrder;
	}
	public void setSalesOrder(List<SalesOrder> salesOrder) {
		this.salesOrder = salesOrder;
	}
   
	
}
