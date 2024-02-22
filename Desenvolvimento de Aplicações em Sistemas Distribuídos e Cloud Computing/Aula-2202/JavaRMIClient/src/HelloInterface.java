import java.rmi.Remote;
import java.rmi.RemoteException;

public interface HelloInterface extends Remote{
	void printMessage() throws RemoteException;
}
