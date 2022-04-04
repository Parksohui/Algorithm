import sys
from collections import deque

def bfs(l, start, end, depth):
    dx=[-2,-2,-1,-1,2,2,1,1] # 한 번에 이동할 수 있는 칸
    dy=[-1,1,-2,2,-1,1,-2,2]

    queue=deque([start])
    visited=[[0]*l for i in range(l)] # 방문 여부
    visited[start[0]][start[1]]=1

    flag=0

    while queue:
        temp=queue.popleft()
        for i in range(8):
            x=temp[0]+dx[i]
            y=temp[1]+dy[i]
            if x>=0 and x<l and y>=0 and y<l: # 체스판 범위 안이라면
                if visited[x][y]==0:
                    visited[x][y]=1 # 방문
                    depth[x][y]=depth[temp[0]][temp[1]]+1 # 이동 수
                    queue.append([x,y])
                    if x==end[0] and y==end[1]: # 이동하려고 하는 칸에 도착
                        flag=1
                        break
        if flag==1:
            break


if __name__=='__main__':
    t=int(input())

    for i in range(t):
        l=int(sys.stdin.readline  ().strip())
        x,y=map(int, sys.stdin.readline().split()) # 현재 위치
        a,b=map(int, sys.stdin.readline().split()) # 이동 위치

        depth=[[0]*l for j in range(l)]
        bfs(l, [x,y], [a,b], depth)

        print(depth[a][b])