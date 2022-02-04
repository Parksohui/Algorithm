import sys
from collections import deque

def bfs(graph, start, depth):
    queue=deque([start])
    while queue:
        temp=queue.popleft()
        for i in graph[temp]:
            if depth[i]==0 and i!=start: #아직 방문하지 않았으면
                depth[i]=depth[temp]+1
                queue.append(i)

if __name__=='__main__':
    #도시의 개수, 도로의 개수, 거리 정보, 출발 도시의 번호
    N,M,K,X=map(int,sys.stdin.readline().split())

    graph={}
    depth=[0]*(N+1)
    for i in range(N):
        graph[i+1]=[]

    for i in range(M):
        A,B=map(int,sys.stdin.readline().split())
        graph[A].append(B)

    bfs(graph,X,depth)

    result=[]
    for i in range(N):
        if depth[i+1]==K: # 최단 거리가 K
            result.append(i+1)

    if len(result)==0: # 하나도 존재하지 않으면
        print(-1)
    else: # 도시의 번호를 오름차순으로 출력
        result.sort()
        for i in result:
            print(i)