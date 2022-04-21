import sys
from collections import deque

if __name__=='__main__':
    n,m,k=map(int,sys.stdin.readline().split()) # 세로 길이, 가로 길이, 개수

    graph=[[0]*m for i in range(n)]
    for i in range(k): # 좌표 입력
        r,c=map(int,sys.stdin.readline().split())
        graph[r-1][c-1]=1
    
    area=[]
    dx=[-1,1,0,0] # 상하좌우
    dy=[0,0,-1,1]
    
    for i in range(n):
        for j in range(m):
            if graph[i][j]==1:
                queue=deque([[i,j]])
                graph[i][j]=0
                cnt=1
                
                while queue:
                    temp=queue.popleft()
                    for r in range(4):
                        x=temp[0]+dx[r]
                        y=temp[1]+dy[r]
                        if x>=0 and x<n and y>=0 and y<m: # 좌표 범위 안
                            if graph[x][y]==1:
                                graph[x][y]=0
                                queue.append([x,y])
                                cnt+=1 # 크기 +1
                area.append(cnt)
    print(max(area)) # 가장 큰 값 출력