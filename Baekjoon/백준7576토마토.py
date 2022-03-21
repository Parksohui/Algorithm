import sys
from collections import deque

def bfs(graph, queue, visited, depth):
    dx=[-1,1,0,0] # 상하좌우
    dy=[0,0,-1,1]

    while queue:
        temp=queue.popleft()
        for i in range(4):
            x=temp[0]+dx[i]
            y=temp[1]+dy[i]
            if x>=0 and x<len(graph) and y>=0 and y<len(graph[0]): # 상자 범위에 든다면
                if visited[x][y]==0: # 방문 x, 토마토 안익음
                    queue.append([x,y])
                    visited[x][y]=1 # 방문
                    depth[x][y]=depth[temp[0]][temp[1]]+1 # 날짜 구하기

if __name__=='__main__':
    m,n=map(int, sys.stdin.readline().split())

    graph=[]
    answer=0 # 최소 날짜
    for i in range(n):
        temp=list(map(int ,sys.stdin.readline().split()))
        graph.append(temp)

    visited=[[0]*m for i in range(n)] # 방문 여부
    depth=[[0]*m for i in range(n)] # 최소 날짜 구하기

    queue=deque([])
    for i in range(n):
        for j in range(m):
            if visited[i][j]==0 and graph[i][j]==1: # 방문 x, 익은 토마토
                queue.append([i,j])
                visited[i][j]=1
            if graph[i][j]==-1: # 토마토가 들어있지 않음
                visited[i][j]=1

    bfs(graph, queue, visited, depth)

    flag=0
    for i in range(n):
        for j in range(m):
            if visited[i][j]==0: # 토마토가 모두 익지 못하는 경우
                flag=1
                break
            else:
                if answer<depth[i][j]: # 최소 날짜 구하기
                    answer=depth[i][j]

    if flag==1:
        print(-1)
    else:
        print(answer)
