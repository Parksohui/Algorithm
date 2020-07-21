import java.util.Scanner;

public class 백준1380earring {

	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);
		
		int scenario=-1;
		int number=0;
		while(true) {
			scenario=input.nextInt();
			input.nextLine();
			if(scenario == 0) {
				break;
			}
			String array[]=new String[scenario];
			
			for(int i=0; i<scenario; i++) {
				array[i]=input.nextLine();
			}
			
			int check[]=new int[scenario];
			String temp[]=new String[2*scenario -1];
			for(int i=0; i<scenario; i++) {
				check[i]=0;
			}
			for(int i=0; i<2*scenario-1; i++) {
				int tempnumber=input.nextInt();
				check[tempnumber-1]++;
				temp[i]=input.next();
			}
			for(int i=0; i<scenario; i++) {
				if(check[i]==1) {
					number++;
					System.out.println(number+" "+array[i]);
					break;
				}
			}	
		}
	}
}
