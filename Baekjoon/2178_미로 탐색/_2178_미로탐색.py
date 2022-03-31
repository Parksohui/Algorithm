import sys
from collections import deque

def maze(graph, start, depth):
    dx=[-1,1,0,0] # 상하좌우
    dy=[0,0,-1,1]

    visited = [[0] * len(graph[0]) for i in range(len(graph))] # 방문 여부
    visited[start[0]][start[1]]=1
    queue=deque([start])

    while queue:
        temp=queue.popleft()
        for i in range(4):
            x=temp[0]+dx[i]
            y=temp[1]+dy[i]
            if  x>=0 and x<len(graph) and y>=0 and y<len(graph[0]): # 미로 범위 안이라면
                if graph[x][y]==1 and visited[x][y]==0: # 이동할 수 있으며 아직 방문하지 않았다면
                    queue.append([x,y])
                    visited[x][y]=1
                    depth[x][y]=depth[temp[0]][temp[1]]+1
if __name__=='__main__':
    n,m=map(int, sys.stdin.readline().split())

    graph=[]
    for i in range(n):
        graph.append(list(map(int, sys.stdin.readline().strip())))

    depth = [[0] * m for i in range(n)]
    start=[0,0] # 출발

    maze(graph, start, depth)

    print(depth[n-1][m-1]+1)