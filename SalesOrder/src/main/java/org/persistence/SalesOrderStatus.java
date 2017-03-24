package org.persistence;

import java.io.Serializable;
import javax.persistence.*;

/**
 * Entity implementation class for Entity: SalesOrderStatus
 *
 */
@Entity

public class SalesOrderStatus implements Serializable {

	
	private static final long serialVersionUID = 1L;
	@Id
	@GeneratedValue(strategy= GenerationType.AUTO)

	private long id;

	public SalesOrderStatus() {
		super();
	}
   
	private String status,text;
	
}
