import sys

def friend(graph, start):
    queue=graph.get(start) #자신의 친구
    visited=[start]

    while queue:
        a=queue.pop(0)
        visited.append(a) # 자신의 친구
        visited+=graph.get(a) # 친구의 친구

    result=len(set(visited))-1 # 결혼식에 초대할 사람의 수
    return result


if __name__=='__main__':
    n=int(input())
    m=int(input())

    graph={}
    for i in range(n):
        graph[i+1]=[]

    for i in range(m):
        x,y=map(int, sys.stdin.readline().split())
        graph[x].append(y)
        graph[y].append(x)

    result=friend(graph, 1)
    print(result)