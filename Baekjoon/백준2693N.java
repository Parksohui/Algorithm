import java.util.Arrays;
import java.util.Scanner;

public class 백준2693N {

	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);
		
		int T= input.nextInt();
		
		int [][]array=new int[T][10];
		
		for(int i=0; i<T; i++) {
			for(int k=0; k<10; k++) {
				array[i][k]=input.nextInt();
			}
		}
		
		for(int i=0; i<T; i++) {
			Arrays.sort(array[i]);
			System.out.println(array[i][7]);
		}
	}

}
