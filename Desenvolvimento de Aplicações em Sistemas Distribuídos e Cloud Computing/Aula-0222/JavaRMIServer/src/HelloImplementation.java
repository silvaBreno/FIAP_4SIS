import java.rmi.RemoteException;

public class HelloImplementation implements HelloInterface{

	@Override
	public void printMessage() throws RemoteException {
		// TODO Auto-generated method stub
		System.out.println("Exmplo de utilização de middleware Java RMI");
	}
	
	
}
