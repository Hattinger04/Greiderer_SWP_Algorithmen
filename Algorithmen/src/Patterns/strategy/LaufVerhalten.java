package Patterns.strategy;

public interface LaufVerhalten {

	public void laufen(); 
}

class SchnellLaufen implements LaufVerhalten{

	@Override
	public void laufen() {
		System.out.println("Usain Bolt Laufstil");
	}

}
class LangsamLaufen implements LaufVerhalten{

	@Override
	public void laufen() {
		System.out.println("Langsamer Laufstil");
	}

}
class KomischLaufen implements LaufVerhalten{

	@Override
	public void laufen() {
		System.out.println("Komischer Laufstil");
	}

}
