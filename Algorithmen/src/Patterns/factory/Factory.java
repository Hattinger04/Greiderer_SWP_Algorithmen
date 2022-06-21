package Patterns.factory;

public class Factory {

	public Auto createAuto(Autos auto) {
		switch (auto) {
		case VW:
			return new VW();
		case Audi: 
			return new Audi(); 
		default:
			return null; 
			// or return new VW(); 
			// or throw new Exception("How did you do that?"); 
		}
	}
	
	
	enum Autos {
		VW, Audi
	}
}
