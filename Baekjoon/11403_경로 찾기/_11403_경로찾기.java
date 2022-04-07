import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Queue;

public class _11403_경로찾기 {
	static ArrayList<Integer> bfs(HashMap graph, int visited[], int start) {
		Queue<Integer> queue=new LinkedList<>();
		ArrayList<Integer> result=new ArrayList<>(); // 경로
		
		queue.add(start);
		
		while(queue.size()!=0) {
			int temp=queue.poll();
			ArrayList<Integer> x=(ArrayList<Integer>) graph.get(temp);
			for(int i=0; i<x.size(); i++) {
				if(visited[x.get(i)] == 0) {
					queue.add(x.get(i));
					visited[x.get(i)]=1;
					result.add(x.get(i));
				}
			}
		}
		return result;
	}

	public static void main(String[] args) throws IOException {
		BufferedReader bf=new BufferedReader(new InputStreamReader(System.in));
		
		int n=Integer.parseInt(bf.readLine()); // 정점의 개수
		HashMap<Integer, ArrayList<Integer>> graph=new HashMap<>();
		
		
		for(int i=0; i<n; i++) {
			graph.put(i, new ArrayList<>());
		}
		
		int temp[]=new int[n];
		for(int i=0; i<n; i++) { // 인접 행렬 : i -> j 경로 표시
			String s=bf.readLine();
			for(int j=0; j<n; j++) {
				temp[j]=Integer.parseInt(s.split(" ")[j]);
			}
			for(int j=0; j<n; j++) {
				if(temp[j]==1) {
					ArrayList<Integer> x=graph.get(i);
					x.add(j);
					graph.put(i,x);
				}
			}
		}
		int answer[][]=new int[n][n];
		
		for(int i=0; i<n; i++) {
			int visited[]=new int[n]; // 방문 여부
			ArrayList<Integer> result=bfs(graph,visited,i);
			for(int j=0; j<result.size(); j++) { // i -> j 경로 존재
				answer[i][result.get(j)]=1;
			}
		}
		for(int i=0; i<n; i++) {
			for(int j=0; j<n; j++) {
				System.out.print(answer[i][j]+" ");
			}
			System.out.println();
		}
	}

}
