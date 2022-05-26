import sys
from collections import deque

def baby_shark(arr, shark, shark_size,n):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    visited=[[0]*n for i in range(n)] # 방문 여부
    depth = [[0] * n for i in range(n)] # 거리
    visited[shark[0]][shark[1]]=1
    queue=deque([shark])

    while queue:
        temp=queue.popleft()
        for i in range(4):
            x=temp[0]+dx[i]
            y=temp[1]+dy[i]
            if 0<=x<n and 0<=y<n:
                if arr[x][y]<=shark_size and visited[x][y]==0:
                    visited[x][y]=1
                    depth[x][y]=depth[temp[0]][temp[1]]+1
                    queue.append([x,y])
    return depth

def main():
    n=int(input()) # 공간의 크기

    arr=[]
    for i in range(n):
        arr.append(list(map(int,sys.stdin.readline().split())))

    shark_size=2 # 처음 크기
    for i in range(n): # 처음 위치
        for j in range(n):
            if arr[i][j]==9:
                shark=[i,j]
                arr[i][j]=0

    result=0
    eat_num=0 # 먹은 물고기 수
    while True:
        eat = [] # 작은 물고기
        for i in range(n):
            for j in range(n):
                if arr[i][j]!=0 and arr[i][j]<shark_size:
                    eat.append([i,j])
        depth=baby_shark(arr, shark, shark_size,n)

        min_val=n*n
        if len(eat)==0: # 더 이상 먹을 수 있는 것 x
            break

        flag=False
        for i in eat:
            if depth[i[0]][i[1]]!=0 and min_val>depth[i[0]][i[1]]: # 거리가 가까운 것 찾기
                flag=True
                min_val=depth[i[0]][i[1]]
                min_xy=[i[0], i[1]]
        if flag==True:
            result+=min_val
            eat_num+=1
            shark=min_xy
            arr[shark[0]][shark[1]]=0
        else:
            break
        if eat_num==shark_size: # 자신의 크기와 같은 수의 물고기 먹을때 크기 +1
            shark_size+=1
            eat_num=0
    print(result)

if __name__=="__main__":
    main()