import java.util.Scanner;

public class 백준1769Multiple {

	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);
		
		int X=input.nextInt();
		String Xtemp=Integer.toString(X);
		
		int result=0;
		int turn=0;
		
		while(Xtemp.length()<8) {
			if(Xtemp.length()==1) {
				result+=Integer.parseInt(Xtemp);
			}else {
				turn++;
				for(int i=0; i<Xtemp.length(); i++) {
					result+=Xtemp.charAt(i)-'0';
				}
				Xtemp=Integer.toString(result);
			}
			
			if(result<10) {
				System.out.println(turn);
				if(result%3 ==0) {
					System.out.println("YES");
				}else {
					System.out.println("No");
				}
				break;
			}
			result=0;
		}
	}
}
