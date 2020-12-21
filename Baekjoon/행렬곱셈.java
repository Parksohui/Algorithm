package July;

import java.util.Scanner;

public class 행렬곱셈2740 {

	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);

		int N=input.nextInt();
		int M=input.nextInt();

		int A[][]=new int[N][M];

		for(int i=0; i<N; i++) {
			for(int j=0; j<M; j++) {
				A[i][j]=input.nextInt();
			}
		}
		M=input.nextInt();
		int k=input.nextInt();

		int B[][]=new int[M][k];

		for(int i=0; i<M; i++) {
			for(int j=0; j<k; j++) {
				B[i][j]=input.nextInt();
			}
		}

		int C[][]=new int[N][k];
		int h=0;
		
		for(int i=0; i<N; i++) {
			for(int j=0; j<k; j++) {
				while(h<M) {
					C[i][j]+=A[i][h]*B[h][j];
					h++;
					if(h>=M) {
						h=0;
						break;
					}
				}
			}
		}
		for(int i=0; i<N; i++) {
			for(int j=0; j<k; j++) {
				System.out.print(C[i][j]+" ");
			}
			System.out.println();
		}
	}
}
