import java.util.Scanner;

public class 백준2566Best {

	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);
		
		int array[][]=new int[9][9];
		
		for(int i=0; i<9; i++) {
			for(int j=0; j<9; j++) {
				array[i][j]=input.nextInt();
			}
		}
		int max=array[0][0];
		int a=0;
		int b=0;
		for(int i=0; i<9; i++) {
			for(int j=0; j<9; j++) {
				if(max<array[i][j]) {
					max=array[i][j];
					a=i+1;
					b=j+1;
				}
			}
		}
		System.out.println(max);
		System.out.println(a+" "+b);
		
	}

}
