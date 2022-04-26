import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class _1303_전쟁_전투 {
	static int bfs(String[][] arr, int[][] visited, int[] start, String find) {
		int dx[]= {-1,1,0,0}; // 상하좌우
		int dy[]= {0,0,-1,1};
		
		visited[start[0]][start[1]]=1;
		Queue<int[]> queue=new LinkedList<>();
		queue.add(start);
		
		int cnt=1;
		
		while(queue.size()!=0) {
			int temp[]=queue.poll();
			for(int i=0; i<4; i++) {
				int x=temp[0]+dx[i];
				int y=temp[1]+dy[i];
				if(x>=0 && x<arr.length && y>=0 && y<arr[0].length) { // 범위 안
					if(arr[x][y].equals(find) && visited[x][y]==0) {
						visited[x][y]=1;
						queue.add(new int[] {x,y});
						cnt+=1;
					}
				}
			}
		}
		return cnt;
	}

	public static void main(String[] args) throws IOException{
		BufferedReader bf=new BufferedReader(new InputStreamReader(System.in));
		
		String s=bf.readLine();
		int n=Integer.parseInt(s.split(" ")[0]); // 가로
		int m=Integer.parseInt(s.split(" ")[1]); // 세로
		
		String arr[][]=new String[m][n];
		for(int i=0; i<m; i++) {
			s=bf.readLine();
			for(int j=0; j<n; j++) {
				arr[i][j]=s.split("")[j];
			}
		}
		
		int visited_w[][]=new int[m][n]; // 방문 여부
		int visited_b[][]=new int[m][n];
		int cnt_w=0;
		int cnt_b=0;
		
		for(int i=0; i<m; i++) {
			for(int j=0; j<n; j++) {
				if(arr[i][j].equals("W") && visited_w[i][j]==0) {
					int cnt=bfs(arr, visited_w, new int[] {i,j}, "W");
					cnt_w+=(cnt*cnt);
				}
				if(arr[i][j].equals("B") && visited_b[i][j]==0) {
					int cnt=bfs(arr, visited_b, new int[] {i,j}, "B");
					cnt_b+=(cnt*cnt);
				}
			}
		}
		System.out.println(cnt_w +" "+ cnt_b);

	}

}
