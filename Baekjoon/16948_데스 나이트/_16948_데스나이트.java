import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class _16948_데스나이트 {

	public static void main(String[] args) throws IOException{
		BufferedReader bf=new BufferedReader(new InputStreamReader(System.in));
		
		int n=Integer.parseInt(bf.readLine()); // 체스판의 크기
		int x1=0;
		int y1=0;
		int x2=0;
		int y2=0;
		String s=bf.readLine();
		for(int i=0; i<4; i++) {
			x1=Integer.parseInt(s.split(" ")[0]);
			y1=Integer.parseInt(s.split(" ")[1]);
			x2=Integer.parseInt(s.split(" ")[2]);
			y2=Integer.parseInt(s.split(" ")[3]);
		}
		
		Queue<int []>queue=new LinkedList<>();
		int dx[]= {-2,-2,0,0,2,2}; // 이동
		int dy[]= {-1,1,-2,2,-1,1};
		int visited[][]=new int[n][n]; // 방문 여부
		int cnt[][]=new int[n][n]; // 최소 이동 횟수
		
		queue.add(new int[] {x1,y1});
		visited[x1][y1]=1; 
		int flag=0;
		
		while(queue.size()!=0) {
			int temp[]=queue.poll();
			for(int i=0; i<6; i++) {
				int x=temp[0]+dx[i];
				int y=temp[1]+dy[i];
				if(x>=0 && x<n && y>=0 && y<n) { // 체스판 범위 안
					if(visited[x][y]==0) { // 아직 방문 x
						visited[x][y]=1; // 방문
						cnt[x][y]=cnt[temp[0]][temp[1]]+1; // 이동 횟수 +1
						queue.add(new int[] {x,y});
					}
					if(x==x2 && y==y2) { // 종료 조건
						flag=1;
						break;
					}
				}
			}
			if(flag==1) {
				break;
			}
		}
		if(cnt[x2][y2]==0) {
			System.out.println(-1);
		}else {
			System.out.println(cnt[x2][y2]);
		}
	}
}
