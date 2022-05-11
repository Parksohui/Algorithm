import sys
from collections import deque

def throw_dice(a,b,c,d,e,f):
    temp=[0,0,0,0,0,0]
    temp[0]=dice[a]
    temp[1]=dice[b]
    temp[2]=dice[c]
    temp[3]=dice[d]
    temp[4]=dice[e]
    temp[5]=dice[f]
    return temp

def change_direction(num, A, B):
    if A>B: # 시계 방향
        num+=1
        if num>3:
            num=0
    elif A<B: # 반시계 방향
        num-=1
        if num<0:
            num=3
    return num

def get_score(arr, start):
    c=1
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    queue=deque([start])
    visited=[[0]*len(arr[0]) for i in range(len(arr))] # 방문 여부
    visited[start[0]][start[1]]=1

    while queue:
        temp=queue.popleft()
        for i in range(4):
            x=temp[0]+dx[i]
            y=temp[1]+dy[i]
            if 0<=x<len(arr) and 0<=y<len(arr[0]):
                if arr[x][y]==arr[temp[0]][temp[1]] and visited[x][y]==0:
                    queue.append([x,y])
                    visited[x][y]=1
                    c+=1
    return c

if __name__=='__main__':
    n,m,k=map(int,sys.stdin.readline().split()) # 세로, 가로, 이동하는 횟수

    arr=[]
    for i in range(n): # 지도
        arr.append(list(map(int,sys.stdin.readline().split())))

    dice=[2,1,5,6,4,3]
    direction=1 # 0 = 북, 1 = 동, 2 = 남, 3 = 서

    x=0 # 좌표
    y=0
    cnt=0 # 이동한 횟수
    result=0
    while cnt<k:
        flag = False
        if direction==0: # 북
            if x-1>=0:
                flag=True
                x-=1
                dice=throw_dice(1,2,3,0,4,5)
            else: 
                direction=2

        elif direction==1: # 동
            if y+1<m:
                flag = True
                y+=1
                dice=throw_dice(0,4,2,5,3,1)
            else:
                direction=3

        elif direction==2: # 남
            if x+1<n:
                flag = True
                x+=1
                dice=throw_dice(3,0,1,2,4,5)
            else:
                direction=0
        else: # 서
            if y-1>=0:
                flag = True
                y-=1
                dice=throw_dice(0,5,2,4,1,3)
            else:
                direction=1
        if flag==True:
            result+=(get_score(arr, [x,y]) * arr[x][y]) # 점수
            direction = change_direction(direction, dice[3], arr[x][y]) # 방향 결정
            cnt += 1

    print(result)