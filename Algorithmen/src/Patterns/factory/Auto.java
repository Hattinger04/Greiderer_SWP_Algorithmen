package Patterns.factory;

public interface Auto {
	public String name();

	public int ps();
}

class Audi implements Auto {

	@Override
	public String name() {
		return "Audi";
	}

	@Override
	public int ps() {
		return 250;
	}

}

class VW implements Auto {

	@Override
	public String name() {
		return "VW";
	}

	@Override
	public int ps() {
		return 150;
	}

}
