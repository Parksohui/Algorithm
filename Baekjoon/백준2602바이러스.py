import sys

def bfs(graph, start): #너비 우선 탐색
    visited=[]
    temp=[start]

    while temp:
        a=temp.pop(0)
        if a not in visited: # 아직 방문하지 않았다면
            visited.append(a)
            temp+=graph.get(a)
    return visited

if __name__=='__main__':
    num=int(input())
    pair=int(input())

    graph={}
    for i in range(num): #init
        graph[i+1]=[]

    for i in range(pair): # graph 연결
        a,b=map(int ,sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    print(len(bfs(graph,1))-1) # 1번 컴퓨터는 제외