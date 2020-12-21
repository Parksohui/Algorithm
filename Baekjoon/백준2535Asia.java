import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.Scanner;

public class 백준2535Asia {

	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);

		int N=input.nextInt();

		HashMap<Integer, Integer>attend=new HashMap<Integer, Integer>();
		HashMap<Integer, Integer>number=new HashMap<Integer, Integer>();
		ArrayList<Integer>score=new ArrayList<Integer>();
		int check=0;
		for(int i=0; i<N; i++) {
			int a=input.nextInt();
			int b=input.nextInt();
			int c=input.nextInt();

			attend.put(c, a);
			number.put(c, b);
			score.add(c);
		}
		Collections.sort(score, Collections.reverseOrder());

		ArrayList<Integer>result=new ArrayList<Integer>();

		int tmp=2;
		result.add(attend.get(score.get(0)));
		result.add(attend.get(score.get(1)));
		while(tmp<N) {
			result.add(attend.get(score.get(tmp)));
			if(result.get(0)==result.get(1)&&result.get(1)==result.get(2)&&result.get(0)==result.get(2)) {
				result.remove(2);
				tmp+=1;
			}else {
				break;
			}
		}
		System.out.println(attend.get(score.get(0))+" "+number.get(score.get(0)));
		System.out.println(attend.get(score.get(1))+" "+number.get(score.get(1)));
		System.out.println(attend.get(score.get(tmp))+" "+number.get(score.get(tmp)));

	}
}


