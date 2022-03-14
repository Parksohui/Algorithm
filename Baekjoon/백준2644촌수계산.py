import sys

def bfs(graph, start, depth):
    visited=[False]*n # 방문 여부
    visited[start-1]=True
    queue=[start]
    while queue:
        temp=queue.pop(0)
        for i in graph[temp]:
            if visited[i-1]==False: # 방문 아직 안했으면
                visited[i-1]=True
                depth[i-1]=depth[temp-1]+1
                queue.append(i)

if __name__=='__main__':
    n=int(input()) # 전체 사람의 수
    a,b=map(int, sys.stdin.readline().split()) # 계산해야하는 번호
    m=int(input()) # 부모 자식 수

    graph={}
    depth=[0]*n
    for i in range(n):
        graph[i+1]=[]

    for i in range(m):
       x,y=map(int, sys.stdin.readline().split())
       graph[x].append(y)
       graph[y].append(x)

    bfs(graph, a, depth)

    if depth[b-1]==0: # 촌수 계산 불가
        print(-1)
    else:
        print(depth[b-1])

