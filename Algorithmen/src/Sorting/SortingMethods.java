package Sorting;
/**
 * @author Simon Greiderer
 * 
 * Listing multiple sortingfunctions 
 * 
 * In-Place: 	algorithm who needs for the storage of the data only a consistent amount of data
 * 				in addition to the saved data which doesn't depend on n
 * 
 * Stable: 		algorithm preserves the order of records with equal keys
 *
 *
 * O(n): 		= O notation; is used to describe algorithm to how long / how much
 * 				space (how many steps) it takes to finish
 */
public class SortingMethods {

	public static void main(String[] args) {
		System.out.println("Unsortierte Liste: ");
		int[] list = { 6, 0, 7, 2, 4, 6, 9, 5, 1 , 7, 2, 3, 4, 1};
		String ausgabe = "";

		System.out.println("Sortierte Liste");
		for (int i = 0; i < list.length; i++) {
			ausgabe = ausgabe + list[i] + " ";
		}
		System.out.println(ausgabe);
		ausgabe = "";

		System.out.println("Sortieren: ");

		int[] sort = BubbleSort(list);
		for (int i = 0; i < sort.length; i++) {
			ausgabe = ausgabe + sort[i] + " ";
		}
		System.out.println(ausgabe);
	}

	/**
	 * In-Place
	 * Stable
	 * 
	 * Best Case: O(n)
	 * Average Case: O(n²)
	 * Worst Case: O(n²)
	 * 
	 * Disadvantage: Normally used by small n => inefficient by big n
	 */
	public static int[] InsertionSort(int[] list) {
		for(int i = 0; i < list.length; i++) {
			int key = list[i]; 
			int j = i-1;
			while(j >= 0 && list[j] > key) {
				list[j+1] = list[j];
				j--;
			}
			list[j+1] = key; 
		}
		return list;
	}

	/**
	 * In-Place
	 * Not stable
	 * 
	 * Best Case: O(n²)
	 * Average Case: O(n²)
	 * Worst Case: O(n²)
	 * 
	 * Disadvantage: Always n²
	 */
	public static int[] SelectionSort(int[] list) {
		for (int i = 0; i < list.length; i++) {
			int min_index = i;
			for (int j = i + 1; j < list.length; j++) {
				if (list[j] < list[min_index]) {
					min_index = j;
				}
			}
			if(min_index != i) {
				swapValues(list, i, min_index);
			}
		}
		return list;
	}

	/**
	 * In-Place 
	 * Stable
	 * 
	 * Best Case: O(n)
	 * Average Case: O(n²)
	 * Worst Case: O(n²)
	 * 
	 * Disadvantage: slower in comparison to other algorithm
	 */
	public static int[] BubbleSort(int[] list) {
		for (int i = 0; i < list.length; i++) {
			for (int j = i + 1; j < list.length; j++) {
				if (list[j] < list[i]) {
					swapValues(list, i, j);
				}
			}
		}
		return list;
	}

	public static int[] swapValues(int[] list, int i, int j) {
		int zwischenwert = list[j];
		list[j] = list[i];
		list[i] = zwischenwert;
		return list;
	}
}