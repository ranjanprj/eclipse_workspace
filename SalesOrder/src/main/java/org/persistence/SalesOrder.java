package org.persistence;

import java.io.Serializable;
import java.util.Date;

import javax.persistence.*;

@Entity
@Table(name = "SalesOrder")
public class SalesOrder implements Serializable {

	private static final long serialVersionUID = 1L;
	public enum SO_STATUS{
		ORDERS_READY_FOR_BILLING,ORDERS_PENDING_REVE_REC,ORDERS_IWTH_NO_APPROVAL,ORDERS_NEED_APPROVAL,ORDERS_BLOCKED_FOR_BILLING,ALL_ORDERS
	};
			
	public SalesOrder() {
	}

	@Id 
	@GeneratedValue(strategy= GenerationType.AUTO)
	private long id;

	private String salesOrderNumber,orderType,soldToParty,material,project,clientContractNo,SAPContractNo,sourceOrderNo,SLBWellNumber,approver;
	private String S,BlCat,BillT,DstC,Document,DChl,Dv,DocCa,Address,NameOfSoldToParty,SoldToLoc,Counter,ShPt,PODSTATUS,NET,Curr;
	
	@Temporal(TemporalType.TIMESTAMP)
	private Date salesOrderDate;
	@Temporal(TemporalType.TIMESTAMP)
	private Date billingDate;
	
	
	@OneToOne
	private SalesOrderDetail salesOrderDetails;

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

	public String getOrderType() {
		return orderType;
	}

	public void setOrderType(String orderType) {
		this.orderType = orderType;
	}

	public String getSoldToParty() {
		return soldToParty;
	}

	public void setSoldToParty(String soldToParty) {
		this.soldToParty = soldToParty;
	}

	public String getMaterial() {
		return material;
	}

	public void setMaterial(String material) {
		this.material = material;
	}

	public String getProject() {
		return project;
	}

	public void setProject(String project) {
		this.project = project;
	}

	public String getClientContractNo() {
		return clientContractNo;
	}

	public void setClientContractNo(String clientContractNo) {
		this.clientContractNo = clientContractNo;
	}

	public String getSAPContractNo() {
		return SAPContractNo;
	}

	public void setSAPContractNo(String sAPContractNo) {
		SAPContractNo = sAPContractNo;
	}

	public String getSourceOrderNo() {
		return sourceOrderNo;
	}

	public void setSourceOrderNo(String sourceOrderNo) {
		this.sourceOrderNo = sourceOrderNo;
	}

	public String getSLBWellNumber() {
		return SLBWellNumber;
	}

	public void setSLBWellNumber(String sLBWellNumber) {
		SLBWellNumber = sLBWellNumber;
	}

	public String getApprover() {
		return approver;
	}

	public void setApprover(String approver) {
		this.approver = approver;
	}

	public String getS() {
		return S;
	}

	public void setS(String s) {
		S = s;
	}

	public String getBlCat() {
		return BlCat;
	}

	public void setBlCat(String blCat) {
		BlCat = blCat;
	}

	public String getBillT() {
		return BillT;
	}

	public void setBillT(String billT) {
		BillT = billT;
	}

	public String getDstC() {
		return DstC;
	}

	public void setDstC(String dstC) {
		DstC = dstC;
	}

	public String getDocument() {
		return Document;
	}

	public void setDocument(String document) {
		Document = document;
	}

	public String getDChl() {
		return DChl;
	}

	public void setDChl(String dChl) {
		DChl = dChl;
	}

	public String getDv() {
		return Dv;
	}

	public void setDv(String dv) {
		Dv = dv;
	}

	public String getDocCa() {
		return DocCa;
	}

	public void setDocCa(String docCa) {
		DocCa = docCa;
	}

	public String getAddress() {
		return Address;
	}

	public void setAddress(String address) {
		Address = address;
	}

	public String getNameOfSoldToParty() {
		return NameOfSoldToParty;
	}

	public void setNameOfSoldToParty(String nameOfSoldToParty) {
		NameOfSoldToParty = nameOfSoldToParty;
	}

	public String getSoldToLoc() {
		return SoldToLoc;
	}

	public void setSoldToLoc(String soldToLoc) {
		SoldToLoc = soldToLoc;
	}

	public String getCounter() {
		return Counter;
	}

	public void setCounter(String counter) {
		Counter = counter;
	}

	public String getShPt() {
		return ShPt;
	}

	public void setShPt(String shPt) {
		ShPt = shPt;
	}

	public String getPODSTATUS() {
		return PODSTATUS;
	}

	public void setPODSTATUS(String pODSTATUS) {
		PODSTATUS = pODSTATUS;
	}

	public String getNET() {
		return NET;
	}

	public void setNET(String nET) {
		NET = nET;
	}

	public String getCurr() {
		return Curr;
	}

	public void setCurr(String curr) {
		Curr = curr;
	}

	public Date getSalesOrderDate() {
		return salesOrderDate;
	}

	public void setSalesOrderDate(Date salesOrderDate) {
		this.salesOrderDate = salesOrderDate;
	}

	public Date getBillingDate() {
		return billingDate;
	}

	public void setBillingDate(Date billingDate) {
		this.billingDate = billingDate;
	}

	public SalesOrderDetail getSalesOrderDetails() {
		return salesOrderDetails;
	}

	public void setSalesOrderDetails(SalesOrderDetail salesOrderDetails) {
		this.salesOrderDetails = salesOrderDetails;
	}

	

}