import java.util.Scanner;

public class 백준10988Palindrome {

	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);
		
		String line=input.next();
		
		int finish=line.length()-1;
		int check=0;
		for(int i=0; i<line.length()/2; i++) {
			if(line.charAt(i)==line.charAt(finish)) {
				check++;
			}else {
				break;
			}
			finish--;
		}
		if(check!=line.length()/2) {
			System.out.println("0");
		}else {
			System.out.println("1");
		}
	}
}
