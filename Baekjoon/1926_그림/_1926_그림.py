import sys
from collections import deque

if __name__=='__main__':
    n,m=map(int,sys.stdin.readline().split()) # 세로 크기, 가로 크기

    graph=[]
    visited=[[0]*m for i in range(n)] # 방문 여부
    area=[] # 그림의 넓이
    for i in range(n): # 그림의 정보
        graph.append(list(map(int,sys.stdin.readline().split())))

    for i in range(n):
        for j in range(m):
            if visited[i][j]==0 and graph[i][j]==1: # 방문 x, 그림 o
                queue=deque([[i,j]])
                visited[i][j]=1 
                dx=[-1,1,0,0] # 상하좌우
                dy=[0,0,-1,1]
                cnt=1 # 그림의 넓이
                while queue:
                    temp=queue.popleft()
                    for k in range(4):
                        x=temp[0]+dx[k]
                        y=temp[1]+dy[k]
                        if x>=0 and x<n and y>=0 and y<m: # 도화지 범위 안
                            if graph[x][y]==1 and visited[x][y]==0:
                                visited[x][y]=1
                                queue.append([x,y])
                                cnt+=1
                area.append(cnt) # 그림의 넓이 저장

    if len(area)==0: # 그림이 하나도 없는 경우
        print(0) 
        print(0)
    else:
        print(len(area)) # 그림의 개수
        print(max(area)) # 가장 넓은 그림의 넓이