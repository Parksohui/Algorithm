import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.Scanner;

public class 백준1302BestSeller {

	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);

		int number=input.nextInt();

		HashMap<String, Integer>array=new HashMap();
		ArrayList<String> arraylist=new ArrayList<>();

		for(int i=0; i<number; i++) {
			String key=input.next(); 

			if(array.containsKey(key)) {
				array.put(key, array.get(key)+1);
			}else {
				array.put(key, 1);
			}
		}
		int max=0;
		String maxtemp = null;
		for(String key:array.keySet()) {
			if(max<array.get(key)) {
				max=array.get(key);
				maxtemp=key;
			}
		}
		for(String key:array.keySet()) {
			if(array.get(key)==max) {
				arraylist.add(key);
			}
		}
		Collections.sort(arraylist);
		
		System.out.println(arraylist.get(0));
	}

}
