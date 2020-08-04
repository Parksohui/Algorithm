import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.Scanner;

public class 백준1764Listen {

	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);
		
		int listen=input.nextInt();
		int see=input.nextInt();
		
		ArrayList<String>list=new ArrayList<String>();
		ArrayList<String>result=new ArrayList<String>();

		for(int i=0; i<listen+see; i++) {
			list.add(input.next());
		}
		Collections.sort(list);
		
		int turn=0;
		while(turn<list.size()) {
			if(list.get(turn).equals(list.get(turn+1))) {
				result.add(list.get(turn));
			}
			turn+=1;
			if(turn==list.size()-1) {
				break;
			}
		}
	
		System.out.println(result.size());
		for(int i=0; i<result.size(); i++) {
			System.out.println(result.get(i));
		}
	}
}
