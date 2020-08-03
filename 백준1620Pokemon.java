import java.util.HashMap;
import java.util.Scanner;

public class 백준1620Pokemon {

	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);
		
		int number=input.nextInt();
		int question=input.nextInt();
		
		HashMap<String, Integer> array=new HashMap(); //(포켓몬 이름,숫자)
		String[]arraytemp=new String[number]; //(숫자, 포켓몬이름)
		
		for(int i=0; i<number; i++) {
			String turn=input.next();
			array.put(turn,i+1);
			arraytemp[i]=turn;
		}
		for(int i=0; i<question; i++) {
			if(input.hasNextInt()) { //숫자로 입력했으면
				System.out.println(arraytemp[input.nextInt()-1]); //배열에서 출력
			}else { //숫자 입력이 아니면 string
				String turn=input.next();
				System.out.println(array.get(turn)); //해시맵에서 출력
			}
		}
	}
}
