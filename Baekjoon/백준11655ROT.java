import java.util.Scanner;

public class 백준11655ROT {

	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);
		String line=input.nextLine();
		
		String result="";
		char temp = 0;
		for(int i=0; i<line.length(); i++) {
			temp=line.charAt(i);
			if(line.charAt(i)>=65 && line.charAt(i)<=90) {
				temp=(char)(line.charAt(i)+13);
				if(temp>90) {
					temp=(char)(65+temp-90-1);
				}
				
			}else if(line.charAt(i)>=97 && line.charAt(i)<=122) {
				temp=(char)(line.charAt(i)+13);
				if(temp>122) {
					temp=(char)(97+temp-122-1);
				}
			}
			result+=temp;
		}
		System.out.println(result);
	}
}
