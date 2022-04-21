import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class _1743_음식물피하기 {

	public static void main(String[] args) throws IOException {
		BufferedReader bf=new BufferedReader(new InputStreamReader(System.in));
		
		String s=bf.readLine();
		int n=Integer.parseInt(s.split(" ")[0]); // 세로 길이
		int m=Integer.parseInt(s.split(" ")[1]); // 가로 길이
		int k=Integer.parseInt(s.split(" ")[2]); // 개수
		
		int graph[][]=new int[n][m];
		for(int i=0; i<k; i++) { // 좌표 입력
			s=bf.readLine();
			int r=Integer.parseInt(s.split(" ")[0]);
			int c=Integer.parseInt(s.split(" ")[1]);
			graph[r-1][c-1]=1;
		}
		
		int dx[]= {-1,1,0,0}; // 상하좌우
		int dy[]= {0,0,-1,1};
		int max_area=0; // 가장 큰 값
		
		for(int i=0; i<n; i++) {
			for(int j=0; j<m; j++) {
				if(graph[i][j]==1) {
					Queue<int[]>queue=new LinkedList<>();
					queue.add(new int[] {i,j});
					graph[i][j]=0;
					int cnt=1;
					
					while(queue.size()!=0) {
						int temp[]=queue.poll();
						for(int r=0; r<4; r++) {
							int x=temp[0]+dx[r];
							int y=temp[1]+dy[r];
							if(x>=0 && x<n && y>=0 && y<m) { // 좌표 범위 안
								if(graph[x][y]==1) {
									graph[x][y]=0;
									cnt+=1;
									queue.add(new int[] {x,y});
								}
							}
						}
					}
					if(max_area<cnt) {
						max_area=cnt;
					}
				}
			}
		}
		System.out.println(max_area);
	}
}
