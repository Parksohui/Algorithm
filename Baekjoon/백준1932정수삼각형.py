if __name__=='__main__' :
    n=int(input())

    arr=[]
    for i in range(n):
        arr.append(list(map(int,input().split())))

    dp=[arr[0]] #첫번째 줄 그대로
    for i in range(n-1):
        temp=[]
        for j in range(i+1):
            if j>0: #왼쪽 대각선
                if temp[-1]<dp[i][j]+arr[i+1][j]: #앞에서 더한 값 보다 더 크면
                    temp[-1]=dp[i][j]+arr[i+1][j] #업데이트
            else: # 왼쪽 대각선
                temp.append(dp[i][j] + arr[i + 1][j])
            temp.append(dp[i][j]+arr[i+1][j+1]) #오른쪽 대각선
        dp.append(temp) 

    print(max(dp[-1])) #마지막 줄에서 최댓값 출력
