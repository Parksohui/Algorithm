import sys

if __name__=='__main__' :

    N,M=map(int, sys.stdin.readline().split())

    arr=list(map(int,sys.stdin.readline().split()))

    dp=[arr[0]]
    for i in range(1,N): #합
        dp.append(dp[-1]+arr[i])

    for i in range(M):
        result=0
        section=list(map(int,sys.stdin.readline().split()))

        if section[0]-1>0: #구간
            result=dp[section[1]-1]-dp[section[0]-2]
        else:
            result=dp[section[1]-1]

        print(result)
