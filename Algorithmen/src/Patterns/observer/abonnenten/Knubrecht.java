package Patterns.observer.abonnenten;

import Patterns.observer.Abonnent;
import Patterns.observer.Zeitung;

public class Knubrecht implements Abonnent{

	@Override
	public void erhalteZeitung(Zeitung zeitung) {
		System.out.println("Knubrecht hat Zeitung " + zeitung.getTitel() + " erhalten.");
	}

}
