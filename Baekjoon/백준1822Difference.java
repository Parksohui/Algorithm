import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class 백준1822Difference {

	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);
		
		int a=input.nextInt();
		int b=input.nextInt();
		
		ArrayList<Integer>array=new ArrayList<Integer>();

		
		for(int i=0; i<a; i++) {
			array.add(input.nextInt());
		}
		
		int temp=0;
		int ind=0;
		
		for(int i=0; i<b; i++) {
			temp=input.nextInt();
			ind=array.indexOf(temp);
			if(ind!=-1) {
				array.remove(ind);
			}
		}
		Collections.sort(array);
		System.out.println(array.size());
		if(array.size()!=0) {
			for(int i=0; i<array.size(); i++) {
				System.out.print(array.get(i)+" ");
			}
		}
	}
}
