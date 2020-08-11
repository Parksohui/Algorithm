import java.util.Scanner;

public class 백준4999Ah {

	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);
		
		String a=input.next();
		String b=input.next();
		
		if(a.length()>=b.length()) {
			System.out.println("go");
		}else {
			System.out.println("no");
		}
	}
}
