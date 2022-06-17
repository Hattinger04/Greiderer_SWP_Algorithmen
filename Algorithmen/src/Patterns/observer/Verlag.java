package Patterns.observer;

import java.util.ArrayList;
import java.util.List;

public abstract class Verlag {

	private List<Abonnent> abonnenten = new ArrayList<Abonnent>(); 
	
	public void aboHinzufügen(Abonnent abonnent) {
		abonnenten.add(abonnent); 
	}
	
	public void aboEntfernen(Abonnent abonnent) {
		abonnenten.remove(abonnent); 
	}
	
	protected void verteileZeitung(Zeitung zeitung) {
		for(Abonnent abonnent : abonnenten) {
			abonnent.erhalteZeitung(zeitung);
		}
	}
	
}
