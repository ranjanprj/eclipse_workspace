import javax.persistence.EntityManager;
import javax.persistence.Persistence;


import org.persistence.OrganizationData;
import org.persistence.SLBOrganization;
import org.persistence.SalesOrder;
import org.persistence.SalesOrderDetail;
import org.persistence.SalesOrderHeader;
import org.persistence.SalesOrderHeaderItem;

public class PopulateData  {
	private static final String PUNIT_NAME = "salesorder-persistence";

	public static void main(String[] args){
		EntityManager em = Persistence.createEntityManagerFactory(PUNIT_NAME).createEntityManager();
//		
//		
//		OrganizationData organizationData = new OrganizationData();
//		
//		SLBOrganization slbOrganization = new SLBOrganization();
//		
//		
//		SalesOrderDetail sod = new SalesOrderDetail();
//		
//		SalesOrder so = new SalesOrder();
//		
//		
//		em.getTransaction().begin();
//		em.persist(sod);
//		
//		em.getTransaction().commit();
//		
//		em.getTransaction().begin();
//		so.setSalesOrderDetails(sod);
//		
//		em.persist(so);		
//		em.getTransaction().commit();
		
		populateSalesData(em);
	}
	
	private static void populateSalesData(EntityManager em){
		em.getTransaction().begin();
		SalesOrderHeader salesOrderHeader = new SalesOrderHeader();
		em.persist(salesOrderHeader);
		
		
		SalesOrderHeaderItem salesOrderHeaderItem = new SalesOrderHeaderItem();
		salesOrderHeaderItem.setItemCost(10.00);
		salesOrderHeaderItem.setItemName("Plywood");
		salesOrderHeaderItem.setItemNumber("1223");
		salesOrderHeaderItem.setItemQuantity("12");
		salesOrderHeaderItem.setItemUOM("17X20CM");		
		
		salesOrderHeader.addSalesOrderItems(salesOrderHeaderItem);
		em.getTransaction().commit();
	}

}

