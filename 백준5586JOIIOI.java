import java.util.Scanner;

public class 백준5586JOIIOI {

	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);
		
		String a=input.next();
		int JOI=0;
		int IOI=0;
		
		for(int i=0; i<a.length()-2; i++) {
			if(a.charAt(i)=='J') {
				if(a.charAt(i+1)=='O' && a.charAt(i+2)=='I') {
					JOI++;
				}
			}
			else if(a.charAt(i)=='I') {
				if(a.charAt(i+1)=='O' && a.charAt(i+2)=='I') {
					IOI++;
				}
			}
		}
		System.out.println(JOI);
		System.out.println(IOI);
	}
}
