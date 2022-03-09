import sys

if __name__=='__main__':
    n,m=map(int, sys.stdin.readline().split())

    arr=[]
    for i in range(n):
        arr.append(list(map(int, sys.stdin.readline().split())))

    candy=[[0]*m for i in range(n)]
    candy[0][0]=arr[0][0]

    for i in range(n):
        for j in range(m):
            if i==0 and j==0:
                pass
            elif i==0 : # 왼쪽 값들의 합
                candy[i][j] = candy[i][j-1] + arr[i][j]
            elif j==0 : # 위쪽 값들의 합
                candy[i][j] = candy[i-1][j] + arr[i][j]
            else: # 사탕의 개수가 더 많은 값으로 저장
                if candy[i-1][j]+arr[i][j] > candy[i][j-1]+arr[i][j]:
                    candy[i][j]=candy[i-1][j]+arr[i][j]
                else:
                    candy[i][j] =candy[i][j-1]+arr[i][j]

    print(candy[-1][-1]) # 최종 가져올 수 있는 사탕 개수