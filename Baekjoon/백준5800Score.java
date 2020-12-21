import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class 백준5800Score {

	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);

		int turn=input.nextInt();

		for(int i=0; i<turn; i++) {
			int a=input.nextInt();
			int array[]=new int[a];
			for(int j=0; j<a; j++) {
				array[j]=input.nextInt();
			}

			Arrays.sort(array);
			int max=0;
			for(int j=a-1; j>0; j--) {
				if(max<array[j]-array[j-1]) {
					max=array[j]-array[j-1];
				}
			}
			System.out.println("Class "+(i+1));
			System.out.println("Max "+ array[a-1]+", Min "+array[0]+", Largest gap "+max);
		}
	}
}
