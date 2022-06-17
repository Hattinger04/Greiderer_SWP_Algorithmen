package Patterns.strategy;

public interface BellVerhalten {

	public void bellen();
}

class LeiseBellen implements BellVerhalten {
	@Override
	public void bellen() {
		System.out.println("leises bellen");
	}
}

class KomischBellen implements BellVerhalten {

	@Override
	public void bellen() {
		System.out.println("Komisches Bellen");
	}

}

class LautBellen implements BellVerhalten {
	@Override
	public void bellen() {
		System.out.println("LAUTES BELLEN");
	}
}
