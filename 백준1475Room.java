import java.util.Scanner;

public class 백준1475Room {

	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);
		
		int room=input.nextInt();
		
		String number=Integer.toString(room);
		
		int array[]=new int[number.length()];
		for(int i=0; i<number.length(); i++) {
			array[i]=number.charAt(i)-'0';
		}
		int check[]=new int[10];
		for(int i=0; i<10; i++) {
			check[i]=1;
		}
		
		for(int i=0; i<number.length(); i++) {
			if(array[i] ==6 || array[i]==9) {
				if(check[6]<check[9]) {
					check[9]--;
				}else {
					check[6]--;
				}
			}else {
				check[array[i]]--;
			}
		}
		int min=check[0];
		for(int i=0; i<10; i++) {
			if(min>check[i]) {
				min=check[i];
			}
		}
		if(min<0) {
			min=-min;
		}
		System.out.println(min+1);
	}
}
