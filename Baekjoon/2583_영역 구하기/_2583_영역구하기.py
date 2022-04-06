import sys
from collections import deque

def bfs(graph, start, visited):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    queue=deque([start])
    size=0 # 영역의 넓이

    while queue:
        temp=queue.popleft()
        size+=1
        for i in range(4):
            x=temp[0]+dx[i]
            y=temp[1]+dy[i]
            if x>=0 and x<len(graph) and y>=0 and y<len(graph[0]): # 모눈종이 범위 안이라면
                if visited[x][y]==0:
                    queue.append([x,y])
                    visited[x][y]=1
    return size

if __name__=='__main__':
    m,n,k=map(int, sys.stdin.readline().split())

    graph=[[0]*m for i in range(n)] # 모눈종이
    visited = [[0] * m for i in range(n)] # 방문 여부

    for i in range(k):
        x1,y1,x2,y2=map(int,sys.stdin.readline().split())

        for a in range(x1, x2): # 모눈종이에 직사각형 표시
            for b in range(y1, y2):
                graph[a][b]=1
                visited[a][b]=1

    answer=0 # 영역의 개수
    arr=[] # 영역의 넓이
    for i in range(n):
        for j in range(m):
            if graph[i][j]==0 and visited[i][j]==0: 
                answer+=1
                visited[i][j]=1
                size=bfs(graph,[i,j], visited)
                arr.append(size)
    arr.sort() # 오름차순 정렬
    print(answer)
    print(' '.join(map(str,arr)))