import java.util.Scanner;

public class 백준1436Movie {

	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);
		
		int N=input.nextInt();
		
		int result=0;
		int count=0;
		while(true) {
			result++;
			
			String temp=Integer.toString(result);
			int number=0;
			for(int i=0; i<temp.length()-2; i++) {
				if(temp.charAt(i)=='6') {
					if(temp.charAt(i+1)=='6') {
						if(temp.charAt(i+2)=='6') {
							number++;
						}
					}
				}
				
			}
			if(number>=1) {
				count++;
				if(count==N) {
					System.out.println(result);
					break;
				}
			}
		}
	}
}
