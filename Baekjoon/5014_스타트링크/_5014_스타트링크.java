import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class _5014_스타트링크 {

	public static void main(String[] args) throws IOException{
		BufferedReader bf=new BufferedReader(new InputStreamReader(System.in));
		
		String s=bf.readLine();
		int F = Integer.parseInt(s.split(" ")[0]); // 가장 높은 층
		int S = Integer.parseInt(s.split(" ")[1]); // 현재 있는 층
		int G = Integer.parseInt(s.split(" ")[2]); // 이동하려는 층
		int U = Integer.parseInt(s.split(" ")[3]); // 위
		int D = Integer.parseInt(s.split(" ")[4]); // 아래
		
		int visited[]=new int[F+1]; // 방문 여부
		int depth[]=new int[F+1]; // 눌러야 하는 버튼의 수
		
		Queue<Integer>queue=new LinkedList<>();
		queue.add(S);
		
		int dx[]= {U, -D}; // 이동할 수 있는 층 수
		visited[S]=1;
		int flag=0;
		
		while(queue.size()!=0) {
			int temp=queue.poll();
			for(int i=0; i<2; i++) {
				int x=temp+dx[i];
				if (x<=F && x>0) { // 건물 범위 안
					if(visited[x]==0) { // 아직 방문하지 않은 층
						visited[x]=1; // 방문
						depth[x]=depth[temp]+1;
						queue.add(x);
					}
				}
				if (x==G) { // 도착
					flag=1;
					break;
				}
			}
			if(flag==1) { // 도착
				break;
			}
		}
		if (S!=G && depth[G]==0) { // 엘리베이터를 이용해서 갈 수 없다면
			System.out.println("use the stairs");
		}else {
			System.out.println(depth[G]);
		}
	}
}
