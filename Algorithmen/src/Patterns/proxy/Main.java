package Patterns.proxy;

public class Main {

	public static void main(String[] args) {
		Internet internet = new ProxyInternet();
		try {
			internet.connectTo("google.at");
			internet.connectTo("google.com");
		} catch (Exception e) {
			System.out.println(e);
		}
	}
}
