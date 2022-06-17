package Patterns.observer;

public class TTVerlag extends Verlag {

	private Zeitung zeitung; 
	
	public void setZeitung(Zeitung zeitung) {
		this.zeitung = zeitung;
		// Zeitung wird neu verteilt: 
		verteileZeitung(zeitung);
	}	
	
	public Zeitung getZeitung() {
		return zeitung;
	}

}
