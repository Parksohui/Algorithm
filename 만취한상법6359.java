package July;

import java.util.Scanner;

public class 만취한상법6359 {

	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);
		
		int turn=input.nextInt();
		int a[]=new int [turn];
		int h=0;
		
		for(int i=0; i<turn; i++) {
			int count=0;
			int n=input.nextInt();
			int array[]=new int[n];
			
			for(int j=0; j<n; j++) {
				for(int k=2; k<=n; k++) {
					if((j+1)%k==0) {
						array[j]++;
					}
				}
			}
			for(int j=0; j<n; j++) {
				if(array[j]%2==0) {
					count++;
				}
			}
			a[h]=count;
			h++;
		}
		for(int i=0; i<h; i++) {
			System.out.println(a[i]);
		}
	}
}
