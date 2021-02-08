from collections import deque

if __name__=='__main__' :
    x=int(input())

    que=deque([i for i in range(1,x+1)])

    while(len(que)!=1):
        que.popleft()
        temp=que.popleft()
        que.append(temp)

    print(que[0])



