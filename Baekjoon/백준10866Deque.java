import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Scanner;

public class 백준10866Deque {

	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);
		
		Deque<Integer>stack=new ArrayDeque<Integer>();
		
		int a=input.nextInt();
		
		for(int i=0; i<a; i++) {
			String line=input.next();
			
			if(line.equals("push_front")) {
				int temp=input.nextInt();
				stack.addFirst(temp);
			}else if(line.equals("push_back")) {
				int temp=input.nextInt();
				stack.addLast(temp);
			}else if(line.equals("pop_front")) {
				if(stack.size()==0) {
					System.out.println(-1);
				}else {
					System.out.println(stack.pollFirst());
				}
			}else if(line.equals("pop_back")) {
				if(stack.size()==0) {
					System.out.println(-1);
				}else {
					System.out.println(stack.pollLast());
				}
			}else if(line.equals("size")) {
				System.out.println(stack.size());
			}else if(line.equals("empty")) {
				if(stack.size()==0) {
					System.out.println("1");
				}else {
					System.out.println("0");
				}
			}else if(line.equals("front")) {
				if(stack.size()==0) {
					System.out.println("-1");
				}else {
					System.out.println(stack.getFirst());
				}
			}else if(line.equals("back")) {
				if(stack.size()==0) {
					System.out.println("-1");
				}else {
					System.out.println(stack.getLast());
				}
			}
		}
	}
}
