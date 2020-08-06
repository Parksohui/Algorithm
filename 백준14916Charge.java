import java.util.Scanner;

public class 백준14916Charge {

	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);
		
		int value=input.nextInt();
		
		int temp=value/5;
		int rest=value%5;
		int result=0;
		int flag=0;
		while(true) {
			if(rest %2 ==0) {
				result=temp+(rest/2);
				break;
			}else {
				if(temp==0) {
					if(rest%2 !=0) {
						flag=1;
						break;
					}
				}
				temp-=1;
				rest+=5;
			}
		}
		if(flag==1) {
			System.out.println("-1");
		}else {
			System.out.println(result);			
		}
	}
}
