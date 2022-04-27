import sys
from collections import deque

def cheese(arr,queue,visited,cheese_temp):
    cheese_cnt = [[0] * m for i in range(n)] # 공기와 접촉한 변 개수
    dx=[-1,1,0,0] # 상하좌우
    dy=[0,0,-1,1]

    while queue:
        temp=queue.popleft()
        for i in range(4):
            x=temp[0]+dx[i]
            y=temp[1]+dy[i]
            if 0<=x<len(arr) and 0<=y<len(arr[0]): # 범위 안
                if arr[x][y]==0 and visited[x][y]==0: # 공기 - 방문 x
                    visited[x][y]=1
                    queue.append([x,y])
                elif arr[x][y]==1: # 치즈
                    if visited[x][y]==0: # 방문 x
                        cheese_cnt[x][y]+=1
                        visited[x][y] = 1
                    else: # 치즈 - 공기 2변 이상
                        cheese_temp.append([x,y])
    return cheese_temp

if __name__=='__main__':
    n,m=map(int,sys.stdin.readline().split())

    arr=[]
    for i in range(n):
        arr.append(list(map(int,sys.stdin.readline().split())))

    visited=[[0]*m for i in range(n)] # 방문 여부

    queue=deque([[0,0]])
    cheese_temp=deque([])
    visited[0][0] = 1

    day=0
    cheese_temp=cheese(arr,queue,visited,cheese_temp)
    for i in cheese_temp: # 치즈 -> 공기
        arr[i[0]][i[1]]=0

    while cheese_temp:
        day+=1
        cheese_temp = cheese(arr, cheese_temp, visited, deque([]))
        for i in cheese_temp:
            arr[i[0]][i[1]] = 0

    print(day)