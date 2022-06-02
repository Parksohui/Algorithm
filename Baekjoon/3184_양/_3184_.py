import sys
from collections import deque

def survival(arr, visited, start, result):
    queue=deque([start])
    sheep=0;wolf=0

    if arr[start[0]][start[1]]=='v': # 늑대
        wolf+=1
    elif arr[start[0]][start[1]]=='o': # 양
        sheep+=1

    dx=[-1,1,0,0] # 상하좌우
    dy=[0,0,-1,1]

    while queue:
        temp=queue.popleft()
        for i in range(4):
            x=temp[0]+dx[i]
            y=temp[1]+dy[i]
            if 0<=x<len(arr) and 0<=y<len(arr[0]) and visited[x][y]==0:
                if arr[x][y]!="#":
                    queue.append([x,y])
                    visited[x][y]=1
                    if arr[x][y]=='v':
                        wolf+=1
                    elif arr[x][y]=='o':
                        sheep+=1
                else:
                    visited[x][y]=1

    if sheep>wolf:
        result[0]+=sheep
    else:
        result[1]+=wolf


def main():
    r,c=map(int, input().split()) # 행, 열

    arr=[]
    for i in range(r):
        arr.append(list(sys.stdin.readline().strip()))

    visited=[[0]*c for i in range(r)] # 방문 여부
    result=[0,0] # 양, 늑대 수
    for i in range(r):
        for j in range(c):
            if arr[i][j]!='#' and visited[i][j]==0: # 울타리가 아니고 아직 방문하지 않았다면
                visited[i][j]=1 # 방문
                survival(arr, visited, [i,j], result)

    print(str(result[0])+" "+ str(result[1]))


if __name__=='__main__':
    main()