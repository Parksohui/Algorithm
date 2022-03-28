import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Stack;

public class _2493_탑 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int n=Integer.parseInt(br.readLine()); // 탑의 수
	
		String arr[]=br.readLine().split(" "); // 탑의 높이
	
		
		Stack<int[]> stack=new Stack<>();
		int[] answer=new int[n];
		
		for(int i=0; i<n; i++) {
			while(true) {
				if(stack.size()==0) { // 레이저 신호 수신하는 탑 존재 x
					answer[i]=0;
					stack.push(new int[] {i+1, Integer.parseInt(arr[i])});
					break;
				}else if(stack.peek()[1]< Integer.parseInt(arr[i])) { // 왼쪽 탑의 높이가 더 낮으면
					stack.pop();
				}else { // 왼쪽 탑의 높이가 높거나 같으면
					answer[i]=stack.peek()[0];
					stack.push(new int[] {i+1, Integer.parseInt(arr[i])});
					break;
				}
			}			
		}
		for(int i=0; i<n; i++) { // 출력
			bw.write(answer[i]+" ");
		}
		bw.flush();
		bw.close();
	}
}
