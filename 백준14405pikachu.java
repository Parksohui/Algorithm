import java.util.Scanner;

public class 백준14405pikachu {

	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);
		
		String in=input.next();
		
		String a="pi";
		String b="ka";
		String c="chu";
		
		int flag=0;
		int i=0;
		while(i<in.length()) {
			if(in.charAt(i) =='p' ) {
				if(i+1>=in.length()) {
					flag=1;
					break;
				}
				else if(in.charAt(i+1)=='i') {
					i+=2;
				}else {
					flag=1;
					break;
				}
			}
			else if(in.charAt(i)=='k') {
				if(i+1>=in.length()) {
					flag=1;
					break;
				}
				else if(in.charAt(i+1)=='a') {
					i+=2;
				}else {
					flag=1;
					break;
				}
			}
			else if(in.charAt(i)=='c') {
				if(i+1>=in.length()) {
					flag=1;
					break;
				}
				else if(in.charAt(i+1)=='h') {
					if(i+2>=in.length()) {
						flag=1;
						break;
					}
					else if(in.charAt(i+2)=='u') {
						i+=3;
					}else {
						flag=1;
						break;
					}
				}else {
					flag=1;
					break;
				}
			}else {
				flag=1;
				break;
			}
			if(i==in.length()) {
				break;
			}
		}

		if(flag==1) {
			System.out.println("NO");
		}else {
			System.out.println("YES");
		}
	}
}
