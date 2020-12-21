import java.util.HashMap;
import java.util.Scanner;

public class 백준2755average {

	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);
		
		HashMap<String, Double>number=new HashMap<>();
		number.put("A+", 4.3);
		number.put("A0", 4.0);
		number.put("A-", 3.7);
		number.put("B+", 3.3);
		number.put("B0", 3.0);
		number.put("B-", 2.7);
		number.put("C+", 2.3);
		number.put("C0", 2.0);
		number.put("C-", 1.7);
		number.put("D+", 1.3);
		number.put("D0", 1.0);
		number.put("D-", 0.7);
		number.put("F", 0.0);
		
		int N=input.nextInt();
		int[]array=new int[N];
		Double[]score=new Double[N];
		for(int i=0; i<N; i++) {
			String tmp=input.next();
			array[i]=input.nextInt();
			String sc=input.next();
			score[i]=number.get(sc);
		}
		Double result=0.0;
		int result_score=0;
		for(int i=0; i<N; i++) {
			result_score+=array[i];
			result+=array[i]*score[i];
		}
		System.out.println(String.format("%.2f", result/result_score));
	}
}
