package org.persistence;

import java.io.Serializable;
import java.util.Date;

import javax.persistence.*;

@Entity
@Table(name = "SalesOrderDetail")
public class SalesOrderDetail implements Serializable {

	private static final long serialVersionUID = 1L;
	public enum SO_STATUS{
		ORDERS_READY_FOR_BILLING,ORDERS_PENDING_REVE_REC,ORDERS_IWTH_NO_APPROVAL,ORDERS_NEED_APPROVAL,ORDERS_BLOCKED_FOR_BILLING,ALL_ORDERS
	};
			
	public SalesOrderDetail() {
	}

	@Id
	@GeneratedValue(strategy= GenerationType.AUTO)

	private long id;

	
	
	private String salesDocType,deliveryBlock,operationalApprover,billingBlock,initialApprover;
	private int netValue;
	private SO_STATUS salesOrderStatus;
	
	@Temporal(TemporalType.TIMESTAMP)
	private Date contractStartDate,contractEndDate,acceptanceDate;

	

	public long getId() {
		return id;
	}

	public void setId(long id) {
		this.id = id;
	}



	public String getSalesDocType() {
		return salesDocType;
	}

	public void setSalesDocType(String salesDocType) {
		this.salesDocType = salesDocType;
	}

	public String getDeliveryBlock() {
		return deliveryBlock;
	}

	public void setDeliveryBlock(String deliveryBlock) {
		this.deliveryBlock = deliveryBlock;
	}

	public String getOperationalApprover() {
		return operationalApprover;
	}

	public void setOperationalApprover(String operationalApprover) {
		this.operationalApprover = operationalApprover;
	}

	public String getBillingBlock() {
		return billingBlock;
	}

	public void setBillingBlock(String billingBlock) {
		this.billingBlock = billingBlock;
	}

	public String getInitialApprover() {
		return initialApprover;
	}

	public void setInitialApprover(String initialApprover) {
		this.initialApprover = initialApprover;
	}

	public int getNetValue() {
		return netValue;
	}

	public void setNetValue(int netValue) {
		this.netValue = netValue;
	}

	public SO_STATUS getSalesOrderStatus() {
		return salesOrderStatus;
	}

	public void setSalesOrderStatus(SO_STATUS salesOrderStatus) {
		this.salesOrderStatus = salesOrderStatus;
	}


	public Date getContractStartDate() {
		return contractStartDate;
	}

	public void setContractStartDate(Date contractStartDate) {
		this.contractStartDate = contractStartDate;
	}

	public Date getContractEndDate() {
		return contractEndDate;
	}

	public void setContractEndDate(Date contractEndDate) {
		this.contractEndDate = contractEndDate;
	}

	public Date getAcceptanceDate() {
		return acceptanceDate;
	}

	public void setAcceptanceDate(Date acceptanceDate) {
		this.acceptanceDate = acceptanceDate;
	}
	
	

}