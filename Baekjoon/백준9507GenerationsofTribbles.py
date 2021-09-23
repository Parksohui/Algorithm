if __name__=='__main__':
    t=int(input())

    arr=[]
    for i in range(t):
        x=int(input())
        arr.append(x)

    dp=[1,1,2,4]
    find=max(arr) # 최댓값

    if find>3:
        for i in range(4,find+1):
            dp.append(dp[i-1]+dp[i-2]+dp[i-3]+dp[i-4])

    for i in arr:
        print(dp[i])
