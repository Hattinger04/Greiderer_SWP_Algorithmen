package Patterns.observer.abonnenten;

import Patterns.observer.Abonnent;
import Patterns.observer.Zeitung;

public class Kunibert implements Abonnent {
	
	@Override
	public void erhalteZeitung(Zeitung zeitung) {
		System.out.println("Kunibert hat Zeitung " + zeitung.getTitel() + " erhalten.");
	}

}
