import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Queue;

public class _16928_뱀과사다리게임 {

	public static void main(String[] args) throws IOException {
		BufferedReader bf=new BufferedReader(new InputStreamReader(System.in));
		
		String s=bf.readLine();
		int n=Integer.parseInt(s.split(" ")[0]); // 사다리의 수
		int m=Integer.parseInt(s.split(" ")[1]); // 뱀의 수
		
		HashMap<Integer, Integer> info=new HashMap<>();
		
		for(int i=0; i<n+m; i++) { // 사다리, 뱀 정보
			s=bf.readLine();
			int x=Integer.parseInt(s.split(" ")[0]);
			int y=Integer.parseInt(s.split(" ")[1]);
			info.put(x, y);
		}
		
		int visited[]=new int[101]; // 방문 여부
		int depth[]=new int[101]; // 주사위
		
		Queue<Integer>queue=new LinkedList<>();
		queue.add(1); // 1번 칸에서 시작
		visited[1]=1;
		int dx[]= {1,2,3,4,5,6}; // 주사위
		int flag=0;
		
		while(queue.size()!=0) {
			int temp=queue.poll();
			for(int i=0; i<6; i++) {
				int x=temp+dx[i];
				if (x<=100 && visited[x]==0) { // 게임판 범위 안, 아직 방문하지 않았으면
					visited[x]=1;
					if(info.containsKey(x)) { // 사다리, 뱀 존재
						if(visited[info.get(x)]==0) { // 아직 방문하지 않았으면
							queue.add(info.get(x));
							visited[info.get(x)]=1;
							depth[info.get(x)]=depth[temp]+1;
						}
					}else { // 사다리, 뱀 없다면
						queue.add(x);
						depth[x]=depth[temp]+1;
					}
					if(x==100) { // 종료
						flag=1;
						break;
					}
				}
			}
			if(flag==1) { // 종료
				break;
			}
		}
		System.out.println(depth[100]);
	}

}
