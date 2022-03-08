import sys

def bfs(graph, start, depth):
    queue=[start]
    while queue:
        temp=queue.pop(0)
        for i in graph[temp]:
            if depth[i]==0 and i!=start: # 아직 방문하지 않았으면
                depth[i]=depth[temp]+1
                queue.append(i)

if __name__=='__main__':
    n,m=map(int, sys.stdin.readline().split()) # 유저의 수, 친구 관계의 수

    friend={}
    for i in range(n):
        friend[i+1]=[]

    for i in range(m): # 친구 관계
        a,b=map(int, sys.stdin.readline().split())
        friend[a].append(b)
        friend[b].append(a)

    result=[0]*(n+1)
    for i in range(1,n+1): 
        depth = [0] * (n + 1)
        bfs(friend, i, depth)
        result[i]=sum(depth) # 단계의 합

    answer=result.index(min(result[1::])) # 케빈 베이컨의 수가 가장 작은 사람
    print(answer)
