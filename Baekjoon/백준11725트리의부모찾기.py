import sys

def bfs(graph, start, result):
    visited=[False]*len(result) # 방문 여부
    visited[start-1]=True
    queue=[start]
    while queue:
        temp=queue.pop(0)
        for i in graph[temp]:
            if visited[i-1]==False: # 아직 방문하지 않았다면
                visited[i-1]=True # 방문
                result[i-1]=temp # 부모 노드 저장
                queue.append(i)

if __name__=='__main__':
    n=int(input()) # 노드의 개수

    graph={}
    for i in range(1,n+1):
        graph[i]=[]

    for i in range(n-1):
        x,y=map(int ,sys.stdin.readline().split()) # 연결된 두 정점
        graph[x].append(y)
        graph[y].append(x)

    result=[0]*n
    bfs(graph, 1,result)

    for i in range(1,n):
        print(result[i])
