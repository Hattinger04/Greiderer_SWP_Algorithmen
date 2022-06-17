package Patterns;
/**
 * 
 * @author Simon Greiderer
 *
 * Singelton Pattern
 *
 */
public class Singelton {

	private static Singelton instance = new Singelton(); 

	private Singelton() {}

	public static Singelton getInstance() {
		return instance; 
	}
}
