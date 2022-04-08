import sys
from collections import deque

if __name__=='__main__':
    f,s,g,u,d=map(int ,sys.stdin.readline().split()) # 가장 높은 층, 현재 있는 층, 이동하려는 층, 위, 아래

    visited=[0]*(f+1) # 방문 여부
    depth=[0]*(f+1) # 눌러야 하는 버튼의 수

    queue=deque([s])

    dx=[u,-d] # 이동할 수 있는 층 수
    visited[s]=1
    flag=0

    while queue:
        temp=queue.popleft()
        for i in dx:
            x=temp+i
            if x<=f and x>0: # 건물 범위 안
                if visited[x]==0: # 아직 방문하지 않은 층
                    visited[x]=1 # 방문
                    depth[x]=depth[temp]+1
                    queue.append(x)
                if x==g: # 도착
                    flag=1
                    break
        if flag==1: # 도착
            break
    if s!=g and depth[g]==0: # 엘리베이터를 이용해서 갈 수 없다면
        print("use the stairs")
    else: # 눌러야 하는 버튼의 수
        print(depth[g])
