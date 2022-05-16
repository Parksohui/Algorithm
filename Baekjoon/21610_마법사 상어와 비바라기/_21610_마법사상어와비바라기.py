import sys

n,m=map(int,sys.stdin.readline().split())
arr=[] # 바구니
cloud=[[0]*n for i in range(n)] # 구름
for i in range(n):
    arr.append(list(map(int,sys.stdin.readline().split())))

info=[] # 이동의 정보
for i in range(m):
    info.append(list(map(int,sys.stdin.readline().split())))

# 처음 비구름 위치
cloud[n-1][0]=1
cloud[n-1][1]=1
cloud[n-2][0]=1
cloud[n-2][1]=1

# 8개의 방향
dx=[0,-1,-1,-1,0,1,1,1]
dy=[-1,-1,0,1,1,1,0,-1]

# 대각선
dia_x=[-1,-1,1,1]
dia_y=[-1,1,-1,1]

for i in info:
    visited = [[0] * n for v in range(n)]
    for j in range(n):
        for k in range(n):
            if cloud[j][k]==1: # 비구름이 있다면 이동
                x=j+(dx[i[0]-1]*i[1])
                y=k+(dy[i[0]-1]*i[1])
                if x<0:
                    x=n-(-x)%n
                    if x==n:
                        x=0
                elif x>=n:
                    x%=n
                if y<0:
                    y = n - (-y) % n
                    if y==n:
                        y=0
                elif y>=n:
                    y%=n
                visited[x][y]=1 
                arr[x][y]+=1 # 비가 내려 구름 있는 칸의 물의 양 +1
                cloud[j][k]=0 # 구름이 사라짐
    for j in range(n): # 물복사버그
        for k in range(n):
            if visited[j][k]==1: # 물이 증가한 칸
                cnt=0
                for v in range(4): # 대각선
                    x=j+dia_x[v]
                    y=k+dia_y[v]
                    if 0<=x<n and 0<=y<n:
                        if arr[x][y]!=0:
                            cnt+=1
                arr[j][k]+=cnt # 물의 양 증가
    for j in range(n):
        for k in range(n):
            if arr[j][k]>=2 and visited[j][k]==0: # 물의 양 2 이상, 구름이 사라진 칸 x
                cloud[j][k]=1 # 구름 생김
                arr[j][k]-=2 # 물의 양 -2

result=0 # 바구니에 들어있는 물의 양의 합
for i in range(n):
    for j in range(n):
        result+=arr[i][j]

print(result)