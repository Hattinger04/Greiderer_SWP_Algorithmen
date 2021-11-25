public class BinarySearch {

	private static int counter;

	public static void main(String[] args) {

		int[] zahlen = { 12, 22, 44, 66, 77, 80 };
		int zahl = 44; 
		
		System.out.println("??? Suche Iterativ: ");
			
		if (sucheIterativ(zahl, zahlen)) {
			System.out.print("Gefunden ");
		} else {
			System.out.print("Nicht gefunden ");
		}
		System.out.println("Schritte: " + counter);
		System.out.println();
		
		
		System.out.println("Binaere Suche Iterativ: ");
		
		int resultBI = binarySearchIterative(zahlen, zahl);
		if (resultBI == -1) {	
			System.out.println("Nicht gefunden");
		} else {
			System.out.println("Gefunden an Stelle: " + resultBI);
		}
		
		System.out.println();
		
		System.out.println("Binaere Suche Rekursiv: ");
				
		int resultBR = binarySearchRecursive(zahlen, 0, zahlen.length-1, zahl);
		if (resultBR == -1) {
			System.out.println("Nicht gefunden");
		} else {
			System.out.println("Gefunden an Stelle: " + resultBR);
		}
	}

	public static boolean sucheIterativ(int zahl, int[] meineListe) {

		for (int i = 0; i < meineListe.length; i++) {
			counter++;
			if (meineListe[i] == zahl) {
				return true;
			}
		}
		return false;		
	}

	public static int binarySearchIterative(int arr[], int wert) {
		int links = 0, rechts = arr.length - 1;

		while (links <= rechts) {
			
			int mitte = links + (rechts - links) / 2;

			if (arr[mitte] == wert) {
				return mitte;
			}
			if (arr[mitte] < wert) {
				links = mitte + 1;
			} else {
				rechts = mitte - 1;
			}
		}

		return -1;
	}

	public static int binarySearchRecursive(int arr[], int links, int rechts, int wert) {

			int mitte = (rechts + links) / 2;
		
			if(rechts < links) {
				return -1; 
			}
		
			if (arr[mitte] == wert) {
				return mitte;
			}
			if (arr[mitte] > wert) {
				return binarySearchRecursive(arr, links, mitte - 1, wert);
			}
			
			if (arr[mitte] < wert) {
				return binarySearchRecursive(arr, mitte + 1, rechts, wert);
			}
			
			return -1; 
		}

}