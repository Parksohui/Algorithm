import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Scanner;

public class _1068_트리 {
	static int answer=0; //리프 노드의 개수
	
	static void delnode(HashMap graph, int d ) {
		List<Integer> queue=new ArrayList<>();
		queue.add(d);
		
		while(queue.size()!=0) { // queue가 빌 때까지
			int temp=queue.remove(0);
			List<Integer>a=(List<Integer>) graph.get(temp);
			if(a.size()>0) { // 지울 노드와 연결된 노드
				for(int i=0; i<a.size(); i++) {
					queue.add(a.get(i));
				}
			}
			graph.remove(temp);
			
		}
	}

	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);
		
		HashMap<Integer, List> graph=new HashMap<>();
		int n=input.nextInt(); // 노드의 개수
		
		for(int i=0; i<n; i++) { 
			List<Integer> a=new ArrayList<>();
			graph.put(i, a);
		}
		
		int info[]=new int[n];
		
		for(int i=0; i<n; i++) { // 각 노드의 부모
			info[i]=input.nextInt();
		}
		
		for(int i=0; i<info.length; i++) {
			if(info[i]==-1) { // 루트
				continue;
			}else {
				List<Integer>temp=graph.get(info[i]);
				temp.add(i);
				graph.put(info[i], temp);
			}
		}
		int d=input.nextInt(); // 지울 노드의 번호
		delnode(graph,d);
		
		graph.forEach((key, value) ->{
			if(value.contains(d)) { // 지울 노드의 번호가 포함되어있다면 삭제
				List<Integer> delkey=graph.get(key);
				delkey.remove(Integer.valueOf(d));
				graph.put(key, delkey);
			}
			if(value.size()==0) { // 리프 노드의 개수 추가
				answer+=1;
			}
		});
		System.out.println(answer);
	}
}
