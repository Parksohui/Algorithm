import sys
if __name__=='__main__' :
    n=int(sys.stdin.readline().strip())

    dp=[1,2,4]

    arr=[]
    for i in range(n): #입력
        x=int(sys.stdin.readline().strip())
        arr.append(x)

    for i in range(3,max(arr)): #규칙
        dp.append(dp[i - 3] + dp[i - 2] + dp[i - 1])

    for i in arr: #출력
        print(dp[i-1])



