import java.util.Arrays;
import java.util.Scanner;

public class 백준3047ABC {

	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);
		
		int array[]=new int[3];
		
		for(int i=0; i<3; i++) {
			array[i]=input.nextInt();
		}
		Arrays.sort(array);
		
		String a=input.next();
		int result[]=new int[3];
		
		for(int i=0; i<a.length(); i++) {
			if(a.charAt(i)=='A') {
				result[i]=array[0];
			}else if(a.charAt(i)=='B') {
				result[i]=array[1];
			}else {
				result[i]=array[2];
			}
		}
		for(int i=0; i<result.length; i++) {
			System.out.print(result[i]+" ");
		}
	}
}
