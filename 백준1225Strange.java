import java.util.Scanner;

public class 백준1225Strange {

	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);
		
		String A=input.next();
		String B=input.next();
		
		long sum=0;
		int a=0;
		int b=0;
		for(int i=0; i<A.length(); i++) {
			for(int j=0; j<B.length(); j++) {
				a=Character.getNumericValue(A.charAt(i));
				b=Character.getNumericValue(B.charAt(j));
				sum+=a*b;
			}	
		}
		System.out.println(sum);
	}
}
