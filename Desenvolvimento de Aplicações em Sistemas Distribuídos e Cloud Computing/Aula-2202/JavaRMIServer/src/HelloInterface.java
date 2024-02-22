import java.rmi.*;

public interface HelloInterface extends Remote{
	void printMessage() throws RemoteException;
}
