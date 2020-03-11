import java.util.Scanner;

public class 별찍기5 {

	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);
		
		int a=input.nextInt();
		
		int m=1;
		int star=a;
		for(int i=0; i<a; i++) {
			if(i!=0) {
				System.out.println();
			}
			for(int k=0; k<star-1; k++) {
				System.out.print(" ");
			}
			for(int j=0; j<m; j++) {
				System.out.print("*");
			}
			m+=2;
			star-=1;
		}
	}
}
