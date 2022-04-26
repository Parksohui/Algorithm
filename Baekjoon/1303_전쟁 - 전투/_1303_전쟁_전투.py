import sys
from collections import deque

def bfs(arr, visited, start, find):
    dx=[-1,1,0,0] # 상하좌우
    dy=[0,0,-1,1]

    queue=deque([start])
    visited[start[0]][start[1]]=1
    cnt=1

    while queue:
        temp=queue.popleft()
        for i in range(4):
            x=temp[0]+dx[i]
            y=temp[1]+dy[i]
            if 0<=x<len(arr) and 0<=y<len(arr[0]):
                if arr[x][y]==find and visited[x][y]==0:
                    visited[x][y]=1
                    queue.append([x,y])
                    cnt+=1
    return cnt


if __name__=='__main__':
    n,m=map(int,sys.stdin.readline().split()) # 가로, 세로

    arr=[]
    for i in range(m):
        arr.append(list(sys.stdin.readline().strip()))

    visited_w=[[0]*n for i in range(m)]
    visited_b = [[0] * n for i in range(m)]
    w_cnt=0
    b_cnt=0
    for i in range(m):
        for j in range(n):
            if arr[i][j]=='W' and visited_w[i][j]==0:
                cnt=bfs(arr, visited_w, [i,j], 'W')
                w_cnt+=(cnt**2)
            elif arr[i][j]=='B' and visited_b[i][j]==0:
                cnt=bfs(arr, visited_b, [i,j], 'B')
                b_cnt+=(cnt**2)


    print(w_cnt, end=' ')
    print(b_cnt)