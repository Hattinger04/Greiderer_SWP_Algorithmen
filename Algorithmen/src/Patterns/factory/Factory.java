package Patterns.factory;

public class Factory {

	public Auto createAuto(Autos auto) {
		Auto a; 
		switch (auto) {
		case VW:
			a = new VW();
			break;
		case Audi: 
			a = new Audi(); 
			break; 
		default:
			a = new VW(); 
			break;
		}
		return a; 
	}
	
	
	enum Autos {
		VW, Audi
	}
}
