import java.util.Scanner;

public class 백준5523Game {

	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);
		
		int turn=input.nextInt();
		
		int a_result=0;
		int b_reuslt=0;
		
		for(int i=0; i<turn; i++) {
			int a=input.nextInt();
			int b=input.nextInt();	
			if(a>b) {
				a_result++;
			}else if(b>a) {
				b_reuslt++;
			}
		}
		System.out.println(a_result+" "+b_reuslt);
	}

}
