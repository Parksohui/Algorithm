from collections import deque
import sys

if __name__=='__main__' :
    x=list(map(int,sys.stdin.readline().split()))
    y=list(map(int,sys.stdin.readline().split()))

    result = deque([i for i in range(1,x[0]+1)])  # deque사용

    count=0

    for i in y:
        while(i!=result[0]): #2번, 3번 수행 조건
            count+=1

            c=list(result) #slice위해 list로 변환

            #최솟값 찾기 위해 길이 구함
            a=len(c[c.index(i)::])
            b=len(c[:c.index(i)])

            if a<=b: #a가 더 작으면 오른쪽으로 이동 ak, a1, ..., ak-1
                temp=result.pop()
                result.appendleft(temp)
            else: #b가 더 작으면 왼쪽으로 이동 a2, ..., ak, a1
                temp=result.popleft()
                result.append(temp)
        result.popleft() #1번 수행

    print(count)