import sys
from collections import deque

def bfs(graph, visited, start):
    queue=deque([start])
    result=[] # 경로

    while queue:
        temp=queue.popleft()
        for i in graph[temp]:
            if visited[i]==0:
                queue.append(i)
                visited[i]=1
                result.append(i)
    return result

if __name__=='__main__':
    n=int(input()) # 정점의 개수

    graph={}
    for i in range(n):
        graph[i]=[]

    for i in range(n): # 인접 행렬 : i -> j 경로 표시
        s=list(map(int, sys.stdin.readline().split()))
        for j in range(n):
            if s[j]==1:
                graph[i].append(j)

    answer=[[0]*n for i in range(n)]

    for i in range(n):
        visited = [0] * n # 방문 여부
        result=bfs(graph, visited, i)
        for j in result: # i -> j 경로 존재
            answer[i][j]=1

    for i in answer:
        print(' '.join(map(str,i)))