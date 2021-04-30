import sys
from _collections import deque

if __name__=='__main__':
    a=int(input()) #명령의 수
    que=deque()

    for i in range(a):
        task= sys.stdin.readline().split()
        if task[0]=='push': #push
            que.append(task[1])
        elif task[0]=='pop': #pop
            if len(que)==0:
                print(-1)
            else:
                print(que.popleft())
        elif task[0]=='size': #size
            print(len(que))
        elif task[0]=='empty': #empty
            if len(que)==0:
                print(1)
            else:
                print(0)
        elif task[0]=='front': #front
            if len(que)==0:
                print(-1)
            else:
                print(que[0])
        elif task[0]=='back': #back
            if len(que)==0:
                print(-1)
            else:
                print(que[-1])
