package Patterns.factory;

import Patterns.factory.Factory.Autos;

public class Main {

	public static void main(String[] args) {
		Factory factory = new Factory(); 
		Auto auto = factory.createAuto(Autos.Audi); 
		System.out.println(auto.name());
	}
}
