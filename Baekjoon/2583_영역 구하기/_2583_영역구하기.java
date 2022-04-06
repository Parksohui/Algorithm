import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.Queue;

public class _2583_영역구하기 {
	static int bfs(int[][] graph, int [] start, int[][] visited) {
		int dx[]= {-1,1,0,0};
		int dy[]= {0,0,-1,1};
		
		Queue<int []> queue=new LinkedList<>();
		queue.add(start);
		int size=0; // 영역의 넓이
		
		while(queue.size()!=0) {
			int temp[]=queue.poll();
			size+=1;
			for(int i=0; i<4; i++) {
				int x=temp[0]+dx[i];
				int y=temp[1]+dy[i];
				if(x>=0 && x<graph.length && y>=0 && y<graph[0].length) { // 모눈종이 범위 안이라면
					if(visited[x][y]==0) {
						queue.add(new int[] {x,y});
						visited[x][y]=1;
					}
				}
			}
		}
		return size;
	}

	public static void main(String[] args) throws IOException{
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		
		String s=bf.readLine();
		int m= Integer.parseInt(s.split(" ")[0]);
		int n=Integer.parseInt(s.split(" ")[1]);
		int k=Integer.parseInt(s.split(" ")[2]);
		
		int graph[][]=new int[n][m]; // 모눈종이
		int visited[][]=new int[n][m]; // 방문 여부
		
		for(int i=0; i<k; i++) { // 모눈종이에 직사각형 표시
			s=bf.readLine();
			int x1=Integer.parseInt(s.split(" ")[0]);
			int y1=Integer.parseInt(s.split(" ")[1]);
			int x2=Integer.parseInt(s.split(" ")[2]);
			int y2=Integer.parseInt(s.split(" ")[3]);
			
			for(int a=x1; a<x2; a++) {
				for(int b=y1; b<y2; b++) {
					graph[a][b]=1;
					visited[a][b]=1;
				}
			}
		}
		
		int answer=0; // 영역의 개수
		ArrayList<Integer> arr=new ArrayList<>(); // 영역의 넓이
		
		for(int i=0; i<n; i++) {
			for(int j=0; j<m; j++) {
				if(graph[i][j]==0 && visited[i][j]==0) {
					answer+=1;
					visited[i][j]=1;
					int size=bfs(graph,new int[] {i,j}, visited);
					arr.add(size);
				}
			}
		}
		Collections.sort(arr); // 오름차순 정렬
		System.out.println(answer);
		for(int i=0; i<arr.size(); i++) {
			System.out.print(arr.get(i)+" ");
		}
	}

}
