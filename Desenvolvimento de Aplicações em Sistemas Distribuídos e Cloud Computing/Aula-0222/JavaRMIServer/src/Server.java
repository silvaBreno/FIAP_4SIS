import java.rmi.*;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;

public class Server extends HelloImplementation{
	
	public Server() {}
	
	public static void main(String[] args) {
		
		try {
			HelloImplementation obj = new HelloImplementation();
			//forma como a parte Client se comunica com o Server
			HelloInterface stub = (HelloInterface) UnicastRemoteObject.exportObject(obj, 1099);
			
			Registry registry = LocateRegistry.createRegistry(1099);
			registry.bind("HelloInterface", stub);
			System.out.println("Server em execução.....");
			
		} catch (Exception e) {
			// TODO: handle exception
			System.out.println("ERRO gerado: "+ e.getMessage());
			e.printStackTrace();
		}
	}
}
