package Patterns.proxy;

public class RealInternet implements Internet{

	@Override
	public void connectTo(String server) {
		System.out.println("Connecting to " + server);
	}
}
