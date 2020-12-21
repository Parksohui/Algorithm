import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class 백준1159Basketball {

	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);
		
		int a=input.nextInt();
		
		String array[]=new String[a];
		
		for(int i=0; i<a; i++) {
			array[i]=input.next();
		}
		int count=0;
		ArrayList result=new ArrayList<>();
		for(int i=0; i<a; i++) {
			for(int j=i; j<a; j++) {
				if(array[i].charAt(0)==array[j].charAt(0)) {
					count++;
				}
			}
			if(count>=5) {
				if(!result.contains(array[i].charAt(0))) {
					result.add(array[i].charAt(0));
				}
			}
			count=0;
		}
		Collections.sort(result);
		if(result.size()==0) {
			System.out.println("PREDAJA");
		}else {
			for(int i=0; i<result.size(); i++) {
				System.out.print(result.get(i));
			}
		}
	}
}
