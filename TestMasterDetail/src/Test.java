

public class Test {
	
	
	public static void main(String[] args){	 
		 	 
		
		try {
			java.net.URL restServiceURL = new java.net.URL("https://api2.successfactors.eu/");
			java.net.HttpURLConnection httpConnection = (java.net.HttpURLConnection) restServiceURL.openConnection();

			httpConnection.setRequestMethod("GET");

			httpConnection.setRequestProperty("Accept", "application/json");
			
			
			message.setProperty("RESPONSE_CODE",httpConnection.getResponseCode());
		} catch (java.io.IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	
	}
}
