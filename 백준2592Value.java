import java.util.Scanner;

public class 백준2592Value {

	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);
		
		int array[]=new int[10];
		
		for(int i=0; i<10; i++) {
			array[i]=input.nextInt();
		}
		int sum=0;
		for(int i=0; i<10; i++) {
			sum+=array[i];
		}
		System.out.println(sum/10);
		
		int count=0;
		int result[]=new int[10];
		for(int i=0; i<10; i++) {
			for(int j=0; j<10; j++) {
				if(array[i]==array[j]) {
					count++;
				}
			}
			result[i]=count;
			count=0;
		}
		int max=result[0];
		int temp=0;
		for(int i=0; i<10; i++) {
			if(max<result[i]) {
				max=result[i];
				temp=i;
			}
		}
		System.out.println(array[temp]);
	}
}
