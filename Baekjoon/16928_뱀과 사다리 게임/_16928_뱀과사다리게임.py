import sys
from collections import deque

if __name__=='__main__':
    n,m=map(int,sys.stdin.readline().split()) # 사다리의 수, 뱀의 수

    info={}

    for i in range(n+m): # 사다리, 뱀 정보
        x,y=map(int,sys.stdin.readline().split())
        info[x]=y

    visited=[0]*101 # 방문 여부
    depth=[0]*101 # 주사위

    queue=deque([1]) # 1번부터 시작
    visited[1]=1
    dx=[1,2,3,4,5,6] # 주사위
    flag=0

    while queue:
        temp=queue.popleft()
        for i in dx: 
            x=temp+i
            if x<=100: # 게임판 범위 안
                if visited[x]==0 : # 아직 방문하지 않았으면
                    visited[x]=1
                    if x in info: # 사다리, 뱀 있다면
                        if visited[info[x]]==0: # 아직 방문하지 않았으면
                            queue.append(info[x]) # 이동
                            visited[info[x]]=1 # 방문
                            depth[info[x]]=depth[temp]+1 
                    else: # 사다리, 뱀 없다면
                        queue.append(x)
                        depth[x]=depth[temp]+1
                    if x==100: #  종료
                        flag=1
        if flag==1:
            break

    print(depth[100])