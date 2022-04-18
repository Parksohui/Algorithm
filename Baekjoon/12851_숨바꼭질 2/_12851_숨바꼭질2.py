import sys
from collections import deque

if __name__=='__main__':
    x,y=map(int,sys.stdin.readline().split())

    answer=[0]*100001
    queue=deque([x])

    cnt=0
    if x==y: # 현재 위치와 도착할 위치가 같다면
        cnt=1
    else:
        while queue:
            temp=queue.popleft()
            dx = [temp-1, temp+1, temp*2] # 1초 후
            for x in dx:
                if x>=0 and x<=100000 : # 점 범위
                    if answer[x]==0 or answer[x]>=answer[temp]+1:
                        if x == y and answer[x] == answer[temp] + 1: # 방법의 수
                            cnt += 1
                        elif x==y and (answer[x]>answer[temp]+1 or answer[x]==0): # 가장 빠른 시간
                            cnt=1
                        answer[x]=answer[temp]+1
                        queue.append(x)
    print(answer[y]) # 가장 빠른 시간
    print(cnt) # 가장 빠른 시간으로 찾는 방법의 수