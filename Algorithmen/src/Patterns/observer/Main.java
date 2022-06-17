package Patterns.observer;

public class Main {

	public static void main(String[] args) {
		
		TTVerlag verlag = new TTVerlag(); 
		Kunibert kunibert = new Kunibert(); 
		verlag.aboHinzufügen(kunibert);
		verlag.setZeitung(new Zeitung("Guten Tag")); 
		
		verlag.aboHinzufügen(new Knubrecht());
		verlag.setZeitung(new Zeitung("Guten Abend"));
		verlag.aboEntfernen(kunibert);
		
		verlag.setZeitung(new Zeitung("Guten Morgen"));
	}
}
