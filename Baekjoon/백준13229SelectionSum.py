if __name__=='__main__' :
    n=int(input())
    arr=list(map(int,input().split()))

    dp=[arr[0]]
    for i in range(1,n): #합
        dp.append(dp[-1]+arr[i])

    k=int(input())
    for i in range(k):
        a,b=map(int, input().split())
        if a>0: # 구간 합
            answer=dp[b]-dp[a-1]
        else:
            answer=dp[b]
        print(answer)