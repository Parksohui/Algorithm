import java.util.Scanner;

public class 백준10798Vertical {

	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);
		
		String array[]=new String[5];
		
		for(int i=0; i<5; i++) {
			array[i]=input.next();
		}
		for(int i=0; i<15; i++) {
			for(int j=0; j<5; j++) {
				if(array[j].length()>i) {
					System.out.print(array[j].charAt(i));
				}
			}
		}
	}
}
