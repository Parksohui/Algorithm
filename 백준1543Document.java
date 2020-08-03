import java.util.Scanner;

public class 백준1543Document {
	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);

		String text=input.nextLine();
		String find=input.nextLine();

		int start=0;
		int end=find.length();
		int result=0;

		while(true) {
			if(text.length()<find.length()) {
				break;
			}
			String temp=text.substring(start, end);

			if(temp.equals(find)) {
				result++;
				start=end;
				end=end+find.length();
			}else {
				start+=1;
				end+=1;
			}
			if(end-start==find.length() && end>=text.length()+1) {
				break;
			}
		}
		System.out.println(result);
	}
}
