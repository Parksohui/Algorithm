import sys

def dfs(arr, start): # 깊이 우선 탐색
    visit=[]
    temp=[start]

    while temp:
        x=temp.pop(0)
        if x not in visit: # 아직 방문하지 않았다면
            visit.append(x)
            temp=arr.get(x)+temp
    return visit

def bfs(arr, start): # 너비 우선 탐색
    visit=[]
    temp=[start]

    while temp:
        x=temp.pop(0)
        if x not in visit: # 아직 방문하지 않았다면
            visit.append(x)
            temp+=arr.get(x)
    return visit

if __name__=='__main__':
    N,M,V=map(int,sys.stdin.readline().split())

    arr={}
    for i in range(N): #init
        arr[i+1]=[]

    for i in range(M): # 양방향 간선
        a,b=map(int,sys.stdin.readline().split())
        arr[a].append(b)
        arr[b].append(a)

    for key,value in arr.items(): #작은 것 먼저 방문하기 위해 정렬
        value=sorted(value)
        arr[key]=value

    print(' '.join(map(str, dfs(arr,V))))
    print(' '.join(map(str, bfs(arr, V))))
