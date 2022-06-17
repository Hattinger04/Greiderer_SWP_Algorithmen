package Patterns.proxy;

import java.util.ArrayList;
import java.util.List;

public class ProxyInternet implements Internet{

	private Internet internet = new RealInternet(); 
	private static List<String> bannedSites; 
	
	// F�r alle Klassen 
	static {
		bannedSites = new ArrayList<String>(); 
		bannedSites.add("google.at"); 
		bannedSites.add("youtube.com"); 
	}
	
	// �nderung zu RealInternet: �berpr�fung der Serveraddresse
	@Override
	public void connectTo(String server) throws Exception {
		if(bannedSites.contains(server)) {
			throw new Exception("You are not allowed visiting this site!"); 
		}
		internet.connectTo(server);
	}

}
