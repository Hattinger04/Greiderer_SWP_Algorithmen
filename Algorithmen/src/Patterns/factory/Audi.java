package Patterns.factory;

public class Audi implements Auto{

	@Override
	public String name() {
		return "Audi";
	}

	@Override
	public int ps() {
		return 250;
	}

}
