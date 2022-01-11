import sys
from collections import deque

def bfs(graph,start,visited,m,n): #너비 우선 탐색
    dx=[-1,0,0,1] #상좌우하
    dy=[0,-1,1,0]
    temp=deque([start])

    while temp:
        k=temp.popleft()
        visited.append(k) # 방문하면
        for i in range(4):
            x=k[0]+dx[i]
            y=k[1]+dy[i]
            if x>=0 and x<m and y>=0 and y<n: # 범위 확인
                if [x,y] in graph and [x,y] not in visited: # 배추가 있고 아직 방문하지 않았으면
                    graph.remove([x,y]) # 방문할 것이므로 main에서 반복문 돌 필요 없음
                    temp.append([x,y])


if __name__=='__main__':
    t=int(input()) # 테스트 케이스

    for i in range(t):
        m,n,k=map(int,sys.stdin.readline().split())
        visited=[]
        arr=[]
        for i in range(k): # 배추 위치
            x=list(map(int, sys.stdin.readline().split()))
            arr.append(x)

        cnt=0
        for i in arr:
            if i not in visited: # 아직 방문하지 않았으면
                cnt+=1
                bfs(arr,i,visited,m,n)
        print(cnt)
