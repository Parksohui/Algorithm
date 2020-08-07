import java.util.Scanner;

public class 백준10824Number {

	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);
		
		String a=input.next();
		String b=input.next();
		String c=input.next();
		String d=input.next();
		
		long A=Long.valueOf(a+b);
		long B=Long.valueOf(c+d);
		
		System.out.println(A+B);

	}
}
