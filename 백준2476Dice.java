import java.util.Arrays;
import java.util.Scanner;

public class 백준2476Dice {

	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);
		
		int turn=input.nextInt();
		int[]result=new int[turn];
		
		for(int i=0; i<turn; i++) {
			int array[]=new int[3];
			for(int j=0; j<3; j++) {
				array[j]=input.nextInt();
			}
			Arrays.sort(array);
			
			if(array[0]==array[1] && array[1]==array[2] && array[0]==array[2]) { //같은 눈 3개
				result[i]=10000+array[0]*1000;
			}
			else if(array[0]==array[1] || array[1]==array[2]) { //같은 눈 2개
				result[i]=1000+array[1]*100;
			}else { //모두 다른 눈
				int max=array[0];
				for(int j=0; j<3; j++) {
					if(max<array[j]) {
						max=array[j];
					}
				}
				result[i]=max*100;
			}
		}
		int money=result[0];
		for(int i=0; i<turn; i++) {
			if(money<result[i]) {
				money=result[i];
			}
		}
		System.out.println(money);
	}
}
