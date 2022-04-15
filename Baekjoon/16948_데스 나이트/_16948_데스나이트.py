import sys
from collections import deque

if __name__=='__main__':
    n=int(input()) # 체스판의 크기
    x1,y1,x2,y2=map(int,sys.stdin.readline().split())

    queue=deque([[x1,y1]])
    dx=[-2,-2,0,0,2,2] # 이동
    dy=[-1,1,-2,2,-1,1]
    visited=[[0] * n for i in range(n)] # 방문 여부
    cnt = [[-1] * n for i in range(n)] # 최소 이동 횟수

    visited[x1][y1]=1
    cnt[x1][y1]=0
    flag=0


    while queue:
        temp=queue.popleft()
        for i in range(6):
            x=temp[0]+dx[i]
            y=temp[1]+dy[i]
            if x>=0 and x<n and y>=0 and y<n: # 체스판 범위 안
                if visited[x][y]==0: # 아직 방문 x
                    visited[x][y]=1 # 방문
                    cnt[x][y]=cnt[temp[0]][temp[1]]+1 # 이동 횟수 +1
                    queue.append([x,y])
                if x==x2 and y==y2: # 종료 조건
                    flag=1
                    break
        if flag==1:
            break

    print(cnt[x2][y2])