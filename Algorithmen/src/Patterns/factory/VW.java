package Patterns.factory;

public class VW implements Auto{

	@Override
	public String name() {
		return "VW";
	}

	@Override
	public int ps() {
		return 150;
	}

}
