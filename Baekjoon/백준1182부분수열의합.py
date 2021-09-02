import sys
from itertools import combinations  # 조합(순서x)

if __name__=='__main__':
    N,S=map(int, sys.stdin.readline().split())

    arr=list(map(int,sys.stdin.readline().split()))

    result=[]
    for i in range(1,N+1): #모든 경우의 수 찾기 _ 조합 사용
        x=list(combinations(arr,i))
        for j in x: # 튜플 합
            result.append(sum(j))

    cnt=result.count(S)
    print(cnt)