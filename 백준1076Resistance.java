import java.util.HashMap;
import java.util.Scanner;

public class 백준1076Resistance {

	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);
		
		HashMap<String, Integer>arrayvalue=new HashMap<String, Integer>();
		HashMap<String, Integer>array=new HashMap<String, Integer>();
		
		arrayvalue.put("black", 0);
		arrayvalue.put("brown", 1);
		arrayvalue.put("red", 2);
		arrayvalue.put("orange", 3);
		arrayvalue.put("yellow", 4);
		arrayvalue.put("green", 5);
		arrayvalue.put("blue", 6);
		arrayvalue.put("violet", 7);
		arrayvalue.put("grey", 8);
		arrayvalue.put("white", 9);
		
		array.put("black", 1);
		array.put("brown", 10);
		array.put("red", 100);
		array.put("orange", 1000);
		array.put("yellow", 10000);
		array.put("green", 100000);
		array.put("blue", 1000000);
		array.put("violet", 10000000);
		array.put("grey", 100000000);
		array.put("white", 1000000000);
		
		String result="";
		String a=input.next();
		result=Integer.toString(arrayvalue.get(a));
		String b=input.next();
		result+=Integer.toString(arrayvalue.get(b));
		long value=Integer.parseInt(result);
		
		String c=input.next();
		value=value*array.get(c);
		System.out.println(value);
		
	
	}
}
