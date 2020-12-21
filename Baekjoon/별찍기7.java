import java.util.Scanner;

public class 별찍기7 {

	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);
		
		int a=input.nextInt();
		
		int blank=1;
		int star=a;
		for(int i=0; i<a; i++) {
			for(int k=0; k<star-1; k++) {
				System.out.print(" ");
			}
			for(int j=0; j<blank; j++) {
				System.out.print("*");
			}
			blank+=2;
			star-=1;
			System.out.println();
		}
		blank=1;
		star=2*(a-1)-1;
		for(int i=0; i<a-1; i++) {
			for(int j=0; j<blank; j++) {
				System.out.print(" ");
			}
			for(int m=0; m<star; m++) {
				System.out.print("*");
			}
			blank++;
			star-=2;
			System.out.println();
		}
	}
}
