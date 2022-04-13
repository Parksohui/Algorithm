import sys
from collections import deque

def cheese(arr, queue, visited, cheese_temp):
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    while queue:
        temp=queue.popleft()
        for i in range(4):
            x=temp[0]+dx[i]
            y=temp[1]+dy[i]
            if x>=0 and x<len(arr) and y>=0 and y<len(arr[0]): # 판 범위 안
                if arr[x][y]==0 and visited[x][y]==0: # 치즈 x, 방문 x
                    queue.append([x,y])
                    visited[x][y]=1
                elif arr[x][y]==1 and visited[x][y]==0: # 치즈 - 공기
                    cheese_temp.append([x,y])
                    visited[x][y]=1
    return cheese_temp

if __name__=='__main__':
    x,y=map(int,sys.stdin.readline().split())

    arr=[]
    for i in range(x):
        arr.append(list(map(int, sys.stdin.readline().split())))

    visited=[[0]*y for i in range(x)] # 방문

    day=0 # 시간

    cheese_temp = deque([])
    queue=deque([[0,0]])
    cheese_cnt=len(cheese(arr, queue, visited, cheese_temp))


    while cheese_temp:
        day+=1
        cheese_temp=cheese(arr,cheese_temp, visited, deque([]))
        if len(cheese_temp)!=0:
            cheese_cnt=len(cheese_temp)

    print(day) # 시간
    print(cheese_cnt) # 모두 녹기 한 시간 전에 남아있는 치즈 조각 수
