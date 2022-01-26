import sys

def bfs(graph, start,visited):
    queue=[start]

    while queue:
        x=queue.pop(0)
        if x not in visited: # 방문하지 않았다면
            visited.append(x) # 방문
            queue+=graph.get(x)
            queue=list(set(queue)) # 중복 제거


if __name__=='__main__':
    n,m=map(int, sys.stdin.readline().split())

    graph={}

    for i in range(n): #init
        graph[i+1]=[]

    for i in range(m): #방향 없는 그래프
        x,y=map(int, sys.stdin.readline().split())
        graph[x].append(y)
        graph[y].append(x)

    visited=[]
    result=0
    i=1
    while len(visited)!=n: # 연결 요소 개수 구하기
        if i not in visited:
            bfs(graph, i,visited)
            result += 1
        i+=1

    print(result)
