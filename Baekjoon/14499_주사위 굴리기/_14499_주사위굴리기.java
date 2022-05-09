import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class _14499_주사위굴리기 {
	static int[] throw_dice(int dice[], int a, int b, int c, int d, int e, int f){
		int temp[]= {0,0,0,0,0,0};
		temp[0]=dice[a];
		temp[1]=dice[b];
		temp[2]=dice[c];
		temp[3]=dice[d];
		temp[4]=dice[e];
		temp[5]=dice[f];
		
		return temp;
	}

	public static void main(String[] args)throws IOException {
		BufferedReader bf=new BufferedReader(new InputStreamReader(System.in));
		
		String s=bf.readLine();
		int n=Integer.parseInt(s.split(" ")[0]); // 세로
		int m=Integer.parseInt(s.split(" ")[1]); // 가로
		int x=Integer.parseInt(s.split(" ")[2]); // 주사위 좌표
		int y=Integer.parseInt(s.split(" ")[3]);
		int k=Integer.parseInt(s.split(" ")[4]); // 명령의 개수
		
		int arr[][]=new int[n][m]; // 지도
		for(int i=0; i<n; i++) {
			s=bf.readLine();
			for(int j=0; j<m; j++) {
				arr[i][j]=Integer.parseInt(s.split(" ")[j]);
			}
		}
		
		int command[]=new int[k]; // 명령
		s=bf.readLine();
		for(int i=0; i<k; i++) {
			command[i]=Integer.parseInt(s.split(" ")[i]);
		}
		
		int dice[]= {0,0,0,0,0,0};
		
		for(int i=0; i<k; i++) {
			boolean flag=false;
			if(command[i]==1) { // 동
				if(y+1<m) {
					y+=1;
					flag=true;
					dice=throw_dice(dice, 0, 4, 2, 5, 3, 1);
				}
			}
			else if(command[i]==2) { // 서
				if(y-1>=0) {
					y-=1;
					flag=true;
					dice=throw_dice(dice, 0, 5, 2, 4, 1, 3);
				}
			}
			else if(command[i]==3) { // 북
				if(x-1>=0) {
					x-=1;
					flag=true;
					dice=throw_dice(dice, 1, 2, 3, 0, 4, 5);
				}
			}
			else if(command[i]==4) { // 남
				if(x+1<n) {
					x+=1;
					flag=true;
					dice=throw_dice(dice, 3, 0, 1, 2, 4, 5);
				}
			}
			if(flag==true) {
				if(arr[x][y]==0) {
					arr[x][y]=dice[3];
				}else {
					dice[3]=arr[x][y];
					arr[x][y]=0;
				}
				System.out.println(dice[1]);
			}
		}
	}
}
