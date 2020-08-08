import java.util.Scanner;

public class 백준10870Fibo {
	static int fibo(int n) {
		if(n==0) {
			return 0;
		}else if(n==1) {
			return 1;
		}else {
			return fibo(n-1)+fibo(n-2);
		}
	}

	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);
		
		int n=input.nextInt();
		
		System.out.println(fibo(n));

	}
}
