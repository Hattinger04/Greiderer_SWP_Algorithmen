package Patterns.strategy;

public abstract class Hund {

	private BellVerhalten bellVerhalten; 
	private LaufVerhalten laufVerhalten; 
	
	public void setBellVerhalten(BellVerhalten bellVerhalten) {
		this.bellVerhalten = bellVerhalten;
	}
	
	public void setLaufVerhalten(LaufVerhalten laufVerhalten) {
		this.laufVerhalten = laufVerhalten;
	}
	
	public void bellen() {
		bellVerhalten.bellen();
	}
	public void laufen() {
		laufVerhalten.laufen();
	}
}

class Husky extends Hund {
	public Husky() {
		setBellVerhalten(new LeiseBellen());
		setLaufVerhalten(new SchnellLaufen());
	}
}


class Pudel extends Hund {
	public Pudel() {
		setBellVerhalten(new KomischBellen());
		setLaufVerhalten(new LangsamLaufen());
	}
}
