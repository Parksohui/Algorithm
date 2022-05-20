import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

class _17086_아기상어2{
	static int distance(int[] xy, int[][]arr, int n, int m) {
		Queue<int[]> queue=new LinkedList<>();
		queue.add(xy);
		
		int visited[][]=new int[n][m];
		visited[xy[0]][xy[1]]=1;
		
		int dx[]= {-1,1,0,0,-1,-1,1,1}; // 인접한 8방향
		int dy[]= {0,0,-1,1,-1,1,-1,1};
		
		int d=0;
		while(queue.size()!=0) {
			int temp[]=queue.poll();
			for(int i=0; i<8; i++) {
				int x=temp[0]+dx[i];
				int y=temp[1]+dy[i];
				if(x>=0 && x<n && y>=0 && y<m) {
					if(visited[x][y]==0) {
						d=temp[2]+1;
						if(arr[x][y]==1) {
							return d;
						}else {
							visited[x][y]=1;
							queue.add(new int[] {x,y,d});
						}
					}
				}
			}
		}
		return d;
	}
	public static void main(String args[]) throws Exception{
		BufferedReader bf=new BufferedReader(new InputStreamReader(System.in));
		
		String s=bf.readLine();
		int n=Integer.parseInt(s.split(" ")[0]);
		int m=Integer.parseInt(s.split(" ")[1]);
		
		int[][] arr=new int[n][m];
		for(int i=0; i<n; i++) {
			s=bf.readLine();
			for(int j=0; j<m; j++) {
				arr[i][j]=Integer.parseInt(s.split(" ")[j]);
			}
		}
		int result=0;
		for(int i=0; i<n; i++) {
			for(int j=0; j<m; j++) {
				if(arr[i][j]==0) {
					int temp=distance(new int[] {i,j,0}, arr, n,m);
					if(result<temp) {
						result=temp;
					}
				}
			}
		}
		System.out.println(result);
		}
}

