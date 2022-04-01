import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;

public class _2468_안전영역 {
	static void safe(int visited[][], int a, int b) {
		int dx[]= {-1,1,0,0}; // 상하좌우
		int dy[]= {0,0,-1,1};
		
		Queue<int []> queue=new LinkedList<>();
		queue.add(new int[]{a,b});
		
		while(queue.size()!=0) {
			int temp[]=queue.poll();
			for(int i=0; i<4; i++) {
				int x=temp[0]+dx[i];
				int y=temp[1]+dy[i];
				if(x>=0 && x<visited.length && y>=0 && y<visited[0].length) {
					// 지역 범위 안
					if(visited[x][y]==0) { // 아직 방문하지 않았으면
						queue.add(new int[] {x,y});
						visited[x][y]=1; // 방문
					}
				}
			}
		}
	}
	
	public static void main(String[] args) throws IOException{
		BufferedReader bf=new BufferedReader(new InputStreamReader(System.in));
		
		int n= Integer.parseInt(bf.readLine());
		
		int arr[][]=new int[n][n];
		HashSet<Integer> set=new HashSet<>();
		
		for(int i=0; i<n; i++) { // 높이 정보 저장
			String str=bf.readLine();
			for(int j=0; j<n; j++) {
				int temp=Integer.parseInt(str.split(" ")[j]);
				arr[i][j]=temp;
				set.add(temp); // 지역의 높이
			}
		}
		
		int answer=1; // 전체 지역이 물에 잠기지 않은 경우 -> 1
		
		for(int i:set) {
			int cnt=0;
			int visited[][]=new int[n][n];
			for(int j=0; j<n; j++) {
				for(int k=0; k<n; k++) {
					if(arr[j][k]<=i) { // i 높이 이하 지점
						visited[j][k]=1; // 방문 o
					}
				}
			}
			for(int j=0; j<n; j++) {
				for(int k=0; k<n; k++) {
					if(visited[j][k]==0) { // 아직 방문하지 않았으면
						cnt+=1; // 안전한 영역 개수
						safe(visited,j,k);
					}
				}
			}
			if(answer<cnt) { // 안전한 영역의 최대 개수
				answer=cnt;
			}
		}
		System.out.println(answer);
	}
}
