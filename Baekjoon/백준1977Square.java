
import java.util.ArrayList;
import java.util.Scanner;

public class 백준1977Square {

	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);

		int M=input.nextInt();
		int N=input.nextInt();

		ArrayList<Integer>array=new ArrayList<Integer>();
		int a=1;
		while(true) {
			int temp=a*a;
			if(temp>N) {
				break;
			}
			if(temp>=M && temp<=N) {
				array.add(temp);
			}
			a++;
		}
		int sum=0;
		if(array.size()==0) {
			System.out.println("-1");
		}else {
			for(int i=0; i<array.size(); i++) {
				sum+=array.get(i);
			}
			System.out.println(sum);
			System.out.println(array.get(0));
		}
	}	
}
