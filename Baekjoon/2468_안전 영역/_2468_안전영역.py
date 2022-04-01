import sys
from collections import deque

def safe(visited, a,b):
    dx=[-1,1,0,0] # 상하좌우
    dy=[0,0,-1,1]
    queue=deque([[a,b]])

    while queue:
        temp=queue.popleft()
        for i in range(4):
            x=temp[0]+dx[i]
            y=temp[1]+dy[i]
            if x>=0 and x<len(visited) and y>=0 and y<len(visited[0]): # 지역 범위 안
                if visited[x][y]==0: # 아직 방문하지 않았으면
                    queue.append([x,y])
                    visited[x][y]=1

if __name__=='__main__':
    n=int(input())

    arr=[]
    height=[]
    for i in range(n):
        temp=list(map(int, sys.stdin.readline().split()))
        arr.append(temp)
        height+=temp

    height=set(height) # 지역의 높이

    answer=1 # 전체 지역이 물에 잠기지 않은 경우
    for i in height:
        cnt = 0
        visited=[[0]*n for j in range(n)]
        for j in range(n):
            for k in range(n):
                if arr[j][k]<=i: # i 높이 이하 지점
                    visited[j][k]=1 # 방문 o
        for j in range(n):
            for k in range(n):
                if visited[j][k]==0: # 아직 방문하지 않았으면
                    cnt+=1 # 안전한 영역 개수
                    safe(visited, j, k)
        if answer<cnt: # 안전한 영역의 최대 개수
            answer=cnt
    print(answer)
