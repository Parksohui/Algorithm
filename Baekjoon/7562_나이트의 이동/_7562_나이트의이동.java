import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class _7562_나이트의이동 {
	static void bfs(int l, int start[], int end[], int depth[][]) {
		int dx[]= {-2,-2,-1,-1,2,2,1,1}; // 이동할 수 있는 칸
		int dy[]= {-1,1,-2,2,-1,1,-2,2};
		
		int visited[][]=new int[l][l]; // 방문 여부
		visited[start[0]][start[1]]=1;
		
		Queue<int []> queue=new LinkedList<>();
		queue.add(start);
		
		int flag=0;
		
		while(queue.size()!=0) {
			 int temp[]=queue.poll();
			 for(int i=0; i<8; i++) {
				 int x=temp[0]+dx[i];
				 int y=temp[1]+dy[i];
				 if(x>=0 && x<l && y>=0 && y<l) { // 체스판 범위 안이라면
					 if(visited[x][y]==0) {
						 visited[x][y]=1; // 방문
						 queue.add(new int[] {x,y});
						 depth[x][y]=depth[temp[0]][temp[1]]+1;
						 if(x==end[0] && y==end[1]) { // 이동하려고 하는 칸에 도착
							 flag=1;
							 break;
						 }
					 }
				 }
			 }
			 if(flag==1) {
				 break;
			 }
		}
	}

	public static void main(String[] args) throws IOException {
		BufferedReader bf=new BufferedReader(new InputStreamReader(System.in));
		
		int t=Integer.parseInt(bf.readLine()); // 테스트 케이스
		
		for(int i=0; i<t; i++) {
			int l=Integer.parseInt(bf.readLine()); // 체스판의 한 변의 길이
			
			int start[]=new int[2]; // 현재 있는 칸
			String s=bf.readLine();
			start[0]=Integer.parseInt(s.split(" ")[0]);
			start[1]=Integer.parseInt(s.split(" ")[1]);
			
			int end[]=new int[2]; // 나이트가 이동하려고 하는 칸
			s=bf.readLine();
			end[0]=Integer.parseInt(s.split(" ")[0]);
			end[1]=Integer.parseInt(s.split(" ")[1]);
			
			int depth[][]=new int[l][l];
			bfs(l,start,end,depth);
			
			System.out.println(depth[end[0]][end[1]]);
		}
	}
}
