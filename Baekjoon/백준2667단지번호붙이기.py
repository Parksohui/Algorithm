import sys

def bfs(graph, x,y, visited):
    dx=[-1,0,0,1] #상,좌,우,하
    dy=[0,-1,1,0]
    check=0 # 단지에 속하는 집의 수

    temp=[[x,y]] # start
    while temp:
        x=temp.pop(0)
        if visited[x[0]][x[1]]==False: #아직 방문하지 않았다면
            visited[x[0]][x[1]] = True # 방문
            check+=1
            for i in range(4):
                a=x[0]+dx[i]
                b=x[1]+dy[i]
                if a>=0 and a<len(graph) and b>=0 and b<len(graph): #범위에 속하면
                    if graph[a][b]==1 and visited[a][b]==False: # 집이 있고, 아직 방문하지 않았다면
                        temp.append([a,b])
    return check

if __name__=='__main__':
    num=int(input())

    arr=[]
    for i in range(num):
        x=list(map(int, sys.stdin.readline().strip()))
        arr.append(x)

    visited=[[False]*num for i in range(num)] #방문 표시 배열
    result=[]
    cnt=0
    for i in range(num):
        for j in range(num):
            if arr[i][j]==1 and visited[i][j]==False: # 집이 있고, 아직 방문하지 않았다면
                temp=bfs(arr, i,j, visited)
                result.append(temp)
                cnt+=1 # 단지 수
    result.sort() # 단지내 집의 수를 오름차순으로 정렬
    print(cnt)
    for i in result:
        print(i)