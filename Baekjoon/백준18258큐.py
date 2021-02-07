import sys #입력 빠르게 받기 위해 sys사용
from collections import deque

if __name__=='__main__' :
    x=int(sys.stdin.readline()) #한 라인 입력

    result=deque() #deque사용
    for i in range(x):
        temp=sys.stdin.readline().split()

        if temp[0]=="push":
            result.append(temp[1])
        elif temp[0]=="pop":
            if len(result)==0:
                print(-1)
            else:
                print(result.popleft())
        elif temp[0]=="size":
            print(len(result))
        elif temp[0]=="empty":
            if len(result)==0:
                print(1)
            else:
                print(0)
        elif temp[0]=="front":
            if len(result)==0:
                print(-1)
            else:
                print(result[0])
        else:
            if len(result)==0:
                print(-1)
            else:
                print(result[-1])