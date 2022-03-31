import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class _2178_미로탐색 {
	
	static void maze(int graph[][], int start[], int depth[][]) {
		int dx[]= {-1,1,0,0}; //상하좌우
		int dy[]= {0,0,-1,1};
		
		int visited[][]=new int[graph.length][graph[0].length]; // 방문 여부
		visited[start[0]][start[1]]=1;
		
		Queue<int []> queue=new LinkedList<>();
		queue.add(start);
		
		while(queue.size()!=0) {
			int[] temp=queue.poll();
			for(int i=0; i<4; i++) {
				int x=temp[0]+dx[i];
				int y=temp[1]+dy[i];
				if(x>=0&& x<graph.length && y>=0 && y<graph[0].length) { //미로 범위 안이라면
					if(graph[x][y]==1 && visited[x][y]==0) { // 이동할 수 있으며 아직 방문하지 않았다면
						queue.add(new int[] {x,y});
						visited[x][y]=1;
						depth[x][y]=depth[temp[0]][temp[1]]+1;
					}
				}
			}
		}
	}

	public static void main(String[] args) throws IOException{
		BufferedReader bf=new BufferedReader(new InputStreamReader(System.in));
		
		String str=bf.readLine();
		int n=Integer.parseInt(str.split(" ")[0]);
		int m=Integer.parseInt(str.split(" ")[1]);
		
		int graph[][]=new int[n][m];
		for(int i=0; i<n; i++) {
			str=bf.readLine();
			for(int j=0; j<m; j++) {
				graph[i][j]=Integer.parseInt(str.split("")[j]);
			}
		}
		
		int depth[][]=new int[n][m];
		int start[]= {0,0}; //출발
		
		maze(graph, start, depth);
		
		System.out.println(depth[n-1][m-1]+1);
	}
}
