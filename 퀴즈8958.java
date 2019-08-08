package July;

import java.util.Scanner;

public class 퀴즈8958 {

	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);
		
		int a=input.nextInt();
		String k[]=new String[a];
		int count=1;
		int sum=0;
		
		for(int i=0; i<a; i++) {
			k[i]=input.next();
		}
		
		for(int i=0; i<a; i++) {
			char b[]=new char[k[i].length()];
			for(int j=0; j<k[i].length(); j++) {
				b[j]=k[i].charAt(j);
			}
			for(int j=0; j<k[i].length(); j++) {
				if(b[j]=='O') {
					sum+=count;
					if(j+1==k[i].length()) {
						break;
					}
					if(b[j+1]=='O') {
						count++;
					}if(b[j+1]=='X') {
						count=1;
					}
				}
			}
			System.out.println(sum);
			sum=0;
			count=1;
		}
	}
}
