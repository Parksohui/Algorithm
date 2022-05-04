import sys

if __name__=='__main__':
    n,m=map(int,sys.stdin.readline().split()) # 세로, 가로

    r,c,d=map(int,sys.stdin.readline().split()) # 좌표, 방향

    arr=[]
    visited=[[0]*m for i in range(n)] # 방문 여부
    for i in range(n):
        temp=list(map(int,sys.stdin.readline().split()))
        arr.append(temp)

    location=[r,c,d]
    visited[r][c] = 1
    answer=1
    cnt=0 # 2a번 실행 count

    while location:
        if location[2]==0: # 북 -> 왼쪽
            x=location[0]
            y=location[1]-1
        elif location[2]==1: # 동 -> 왼쪽
            x=location[0]-1
            y=location[1]
        elif location[2]==2: # 남 -> 왼쪽
            x=location[0]
            y=location[1]+1
        else: # 서 -> 왼쪽
            x=location[0]+1
            y=location[1]

        if 0<=x<n and 0<=y<m:
            if visited[x][y]==0 and arr[x][y]==0: # 빈 공간 + 방문 x
                visited[x][y] = 1
                cnt=0
                answer += 1
                location[2]-=1 # 왼쪽 방향으로 회전
                if location[2]<0:
                    location[2]=3
                location=[x,y,location[2]]
            else: # 빈 공간 x
                location[2]-=1 # 왼쪽 방향으로 회전
                cnt+=1
                if location[2]<0:
                    location[2]=3
        if cnt==4: # 2a 연속으로 4번 실행 -> 바로 뒤
            if location[2] == 0:  # 북
                x = location[0] +1
                y = location[1]
            elif location[2] == 1:  # 동
                x = location[0]
                y = location[1]-1
            elif location[2] == 2:  # 남
                x = location[0] -1
                y = location[1]
            else:  # 서
                x = location[0]
                y = location[1]+1

            if 0<=x<n and 0<=y<m:
                if arr[x][y]==1: # 벽
                    location=[]
                else: # 벽 x -> 후진
                    location=[x,y,location[2]]
                    cnt=0
    print(answer)


