import sys
from collections import deque

def change( direction, num):
    before = arr[num]
    if direction==1: # 시계
        before=list(before[-1])+before[:7]
    else: # 반시계
        before=before[1::]+list(before[0])

    return before

arr=[] # 톱니바퀴 상태
temp_arr=[] # 톱니바퀴 돌아가는 상태
for i in range(4): 
    x=list(sys.stdin.readline().strip())
    arr.append(x)
    temp_arr.append(x)

k=int(input()) # 회전 횟수
command=deque([]) # 회전시킨 방법
for i in range(k):
    command.append(list(map(int,sys.stdin.readline().split())))

for i in command:
    visited=[0,0,0,0] # 방문 여부
    ex_command=deque([i])
    visited[i[0]-1]=1
    while ex_command:
        temp=ex_command.popleft()
        temp_arr[temp[0]-1]=change(temp[1], temp[0] - 1) 
        if temp[0]==1: # 1번
            if arr[0][2]!=arr[1][6]: 
                if temp[1]==1: # 시계
                        temp_arr[1]=change(-1, 1)
                        if visited[1]==0:
                            visited[1]=1
                            ex_command.appendleft([2,-1])
                else: # 반시계
                    temp_arr[1]=change(1,1)
                    if visited[1] == 0:
                        visited[1] = 1
                        ex_command.appendleft([2,1])
        elif temp[0]==4: # 4번
            if arr[3][6]!=arr[2][2]: 
                if temp[1]==1: # 시계
                    temp_arr[2]=change(-1,2)
                    if visited[2] == 0:
                        visited[2] = 1
                        ex_command.appendleft([3, -1])
                else: # 반시계
                    temp_arr[2]=change(1,2)
                    if visited[2] == 0:
                        visited[2] = 1
                        ex_command.appendleft([3, 1])
        else: # 2번, 3번 
            if arr[temp[0]-1][2]!=arr[temp[0]][6]:
                if temp[1]==1: # 시계
                    temp_arr[temp[0]]=change(-1, temp[0])
                    if visited[temp[0]] == 0:
                        visited[temp[0]] = 1
                        ex_command.appendleft([temp[0]+1, -1])
                else: # 반시계
                    temp_arr[temp[0]] = change(1,temp[0])
                    if visited[temp[0]] == 0:
                        visited[temp[0]] = 1
                        ex_command.appendleft([temp[0]+1, 1])
            if arr[temp[0]-1][6]!=arr[temp[0]-2][2]:
                if temp[1]==1: # 시계
                    temp_arr[temp[0]-2]=change(-1,temp[0]-2)
                    if visited[temp[0]-2] == 0:
                        visited[temp[0]-2] = 1
                        ex_command.appendleft([temp[0]-1, -1])
                else: # 반시계
                    temp_arr[temp[0]-2]=change(1, temp[0]-2)
                    if visited[temp[0]-2] == 0:
                        visited[temp[0]-2] = 1
                        ex_command.appendleft([temp[0]-1, 1])
    arr=temp_arr[:]

result=0
if arr[0][0]=='1': # 1번
    result+=1
if arr[1][0]=='1': # 2번
    result+=2
if arr[2][0]=='1': # 3번
    result+=4
if arr[3][0]=='1': # 4번
    result+=8

print(result)