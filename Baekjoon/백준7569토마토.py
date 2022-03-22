import sys
from collections import deque

def bfs(graph, queue, visited, depth, n):
    dx=[-1,1,0,0, n, -n] # 상,하,좌,우,아래층,위층
    dy=[0,0,-1,1, 0, 0]
    while queue:
        temp=queue.popleft()
        for i in range(6):
            x=temp[0]+dx[i]
            y=temp[1]+dy[i]
            flag=True
            if x>=0 and x<len(graph) and y>=0 and y<len(graph[0]): #토마토 창고 범위 안
                if visited[x][y]==0 : # 아직 방문하지 않았다면
                    if dx[i]!=n and dx[i]!=-n: # 상하좌우==같은 층
                        if temp[0]//n != x//n:
                            flag=False
                    if flag==True:
                        queue.append([x,y])
                        visited[x][y]=1
                        depth[x][y]=depth[temp[0]][temp[1]]+1

if __name__ =='__main__':
    m,n,h=map(int ,sys.stdin.readline().split())

    graph=[]
    for i in range(n*h):
        graph.append(list(map(int ,sys.stdin.readline().split())))

    visited=[[0]*m for i in range(n*h)] # 방문 여부
    depth=[[0]*m for i in range(n*h)] # day
    start=deque([])

    for i in range(n*h):
        for j in range(m):
            if graph[i][j]==-1: # 토마토가 들어있지 않음
                visited[i][j]=1
            if visited[i][j]==0 and graph[i][j]==1: # 방문x, 익은 토마토
                start.append([i,j])
                visited[i][j]=1
    bfs(graph, start, visited, depth, n)

    answer=-1
    flag=False # 모두 익지 못하는 경우 판별
    for i in range(n*h):
        if flag == True:
            answer=-1
            break
        for j in range(m):
            if visited[i][j]==0: # 익지 못한 토마토
                flag=True
                break
            else: # 최소 날짜 구하기
                if answer<depth[i][j]:
                    answer=depth[i][j]

    print(answer)