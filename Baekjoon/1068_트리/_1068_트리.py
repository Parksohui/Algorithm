import sys

def delnode(graph, start):
    queue=[start]

    while queue:
        temp=queue.pop(0)
        for i in graph[temp]: # 지울 노드와 연결된 노드
            queue.append(i)

        del graph[temp]

if __name__ =='__main__':
    n=int(input()) # 노드의 개수

    graph={}
    for i in range(n):
        graph[i]=[]

    info=list(map(int, sys.stdin.readline().split())) # 각 노드의 부모

    for i in range(len(info)):
        if info[i]==-1: # 루트
            pass
        else:
            graph[info[i]].append(i)

    d=int(input()) # 지울 노드의 번호

    answer=0 # 리프 노드의 개수
    delnode(graph, d)

    for key,value in graph.items():
        if d in value: # 노드 지움
            graph[key].remove(d)
        if len(value)==0: # 리프 노드 개수
            answer+=1

    print(answer)