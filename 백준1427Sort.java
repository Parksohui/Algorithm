import java.util.Arrays;
import java.util.Scanner;

public class 백준1427Sort {

	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);
		
		int N=input.nextInt();
		
		String temp=Integer.toString(N);
		char array[]=new char[temp.length()];
		for(int i=0; i<temp.length(); i++) {
			array[i]=temp.charAt(i);
		}
		Arrays.sort(array);
		for(int i=temp.length()-1; i>=0; i--) {
			System.out.print(array[i]);
		}
	}
}