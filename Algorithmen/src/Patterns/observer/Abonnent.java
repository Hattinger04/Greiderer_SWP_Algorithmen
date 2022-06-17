package Patterns.observer;

public interface Abonnent {
	public void erhalteZeitung(Zeitung zeitung); 
}
class Kunibert implements Abonnent {
	
	@Override
	public void erhalteZeitung(Zeitung zeitung) {
		System.out.println("Kunibert hat Zeitung " + zeitung.getTitel() + " erhalten.");
	}

}
class Knubrecht implements Abonnent{

	@Override
	public void erhalteZeitung(Zeitung zeitung) {
		System.out.println("Knubrecht hat Zeitung " + zeitung.getTitel() + " erhalten.");
	}

}
