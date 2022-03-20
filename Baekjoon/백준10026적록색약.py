import sys

def RGB(graph, i,j, visited, flag): # 그림, x, y, 방문, 적록색약 구분
    dx=[-1,0,0,1] # 상,좌,우,하
    dy=[0,-1,1,0]

    queue=[[i,j]]
    visited[i][j]=1
    while queue:
        a,b=queue.pop(0)
        for i in range(4):
            x=a+dx[i]
            y=b+dy[i]
            if x>=0 and x<len(graph) and y>=0 and y<len(graph): #범위에 속하면
                if flag==0: # 적록색약 x
                    if visited[x][y]==0 and graph[a][b]==graph[x][y] :
                        queue.append([x,y])
                        visited[x][y] = 1
                else: # 적록색약
                    if visited[x][y]==0:
                        if graph[a][b]=='R' or graph[a][b]=='G': # R,G 구분 x
                            if graph[x][y]=='R' or graph[x][y]=='G':
                                queue.append([x,y])
                                visited[x][y] = 1
                        else: # B
                            if graph[a][b]==graph[x][y] :
                                queue.append([x,y])
                                visited[x][y] = 1


if __name__=='__main__':
    n=int(input())

    graph=[]
    visited=[[0] *n for i in range(n)]
    visited_RG_B=[[0] *n for i in range(n)] # 적록색약

    for i in range(n): #input
        graph.append(list(sys.stdin.readline().strip()))

    rgb_cnt=0
    rg_b_cnt=0 # 적록색약
    for i in range(n):
        for j in range(n):
            if visited[i][j]==0: # 방문 x
                rgb_cnt+=1
                RGB(graph, i,j, visited,0)
            if visited_RG_B[i][j]==0: # 적록색약_ 방문 x
                rg_b_cnt+=1
                RGB(graph, i, j, visited_RG_B,1)

    print(rgb_cnt, rg_b_cnt)
