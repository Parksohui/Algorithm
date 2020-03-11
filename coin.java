package August;

import java.util.Scanner;

public class coin11047 {

	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);
		int N=input.nextInt();
		int K=input.nextInt();
		int sum=0;
		
		int array[]=new int[N];
		for(int i=0; i<N; i++) {
			array[i]=input.nextInt();
		}
		for(int i=N-1; i>=0; i--) {
			sum+=K/array[i];
			K=K%array[i];
			if(K==0) {
				break;
			}
		}
		System.out.println(sum);
	}
}
