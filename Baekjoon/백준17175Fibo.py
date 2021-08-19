if __name__=='__main__' :
    n=int(input())

    dp=[1,1,3]

    if n>2:
        for i in range(3,n+1):
            dp.append(dp[i-2]+dp[i-1]+1)

    print(dp[n]%1000000007) #나머지 출력