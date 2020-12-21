import java.util.Scanner;

public class 별찍기8 {

	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);
		
		int a=input.nextInt();
		
		int star=1;
		int blank=a-1;
		for(int i=0; i<a; i++) {
			for(int j=0; j<star; j++) {
				System.out.print("*");
			}
			for(int m=0; m<blank*2; m++) {
				System.out.print(" ");
			}
			for(int k=0; k<star; k++) {
				System.out.print("*");
			}
			System.out.println();
			star+=1;
			blank-=1;
		}
		star=a-1;
		blank=1;
		for(int i=0; i<a; i++) {
			for(int j=0; j<star; j++) {
				System.out.print("*");
			}
			for(int m=0; m<blank*2; m++) {
				System.out.print(" ");
			}
			for(int k=0; k<star; k++) {
				System.out.print("*");
			}
			System.out.println();
			star-=1;
			blank+=1;
		}
	}
}
