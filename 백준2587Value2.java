import java.util.Arrays;
import java.util.Scanner;

public class 백준2587Value2 {

	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);
		
		int array[]=new int[5];
		
		int sum=0;
		for(int i=0; i<5; i++) {
			array[i]=input.nextInt();
			sum+=array[i];
		}
		System.out.println(sum/5);
		Arrays.sort(array);
		
		System.out.println(array[2]);

	}
}
