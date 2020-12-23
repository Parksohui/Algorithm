package winter2021;

import java.util.Scanner;

public class 최소공배수1934 {

	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);
		
		int T=input.nextInt();
		
		for(int i=0; i<T; i++) {
			int A=input.nextInt();
			int B=input.nextInt();
			System.out.println(A*B/gcd(A,B));
			
		}

	}
	
	public static int gcd(int a,int b) {
		if(b==0) return a;
		return gcd(b,a%b);
	}

}
