import java.util.Scanner;

public class 별찍기4 {

	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);

		int a = input.nextInt();
		int j=0;
		int w=a;

		for(int i=0; i<a; i++) {

			for(int k=0; k<j; k++) {
				System.out.print(" ");
			}
			for(int q=w; q>0; q--) {
				System.out.print("*");
			}
			j++;
			w--;
			System.out.println();
		}

	}

}
