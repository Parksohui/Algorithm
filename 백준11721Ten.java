import java.util.Scanner;

public class 백준11721Ten {

	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);
		
		String a=input.next();
		int count=0;
		
		for(int i=0; i<a.length(); i++) {
			count++;
			System.out.print(a.charAt(i));
			if(count==10) {
				System.out.println();
				count=0;
			}
		}
	}
}
