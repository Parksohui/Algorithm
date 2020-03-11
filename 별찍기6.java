import java.util.Scanner;

public class 별찍기6 {

	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);
		
		int a=input.nextInt();
		int blank=0;
		int star=2*a-1;
		for(int i=0; i<a; i++) {
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
