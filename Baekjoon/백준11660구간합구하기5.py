import sys

if __name__=='__main__' :
    N,M=map(int,sys.stdin.readline().split())

    arr=[]
    for i in range(N): # 표 입력
        arr.append(list(map(int,sys.stdin.readline().split())))

    dp=[]
    for i in range(N): # 구간 합
        temp=[]
        for j in range(N):
            if i==0:
                if j==0:
                    temp.append(arr[0][0])
                else:
                    temp.append(temp[-1]+arr[i][j])
            else:
                if j==0:
                    temp.append(dp[i-1][j]+arr[i][j])
                else:
                    temp.append(dp[i-1][j]+temp[-1]-dp[i-1][j-1]+arr[i][j])
        dp.append(temp)

    for i in range(M):
        section=list(map(int,sys.stdin.readline().split())) # [x1,y1,x2,y2]

        if section[0]-1!=0 or section[1]-1!=0:
            if section[0]-1!=0 and section[1]-1!=0:
                result=dp[section[2]-1][section[3]-1]-dp[section[2]-1][section[1]-2]-dp[section[0]-2][section[3]-1]+dp[section[0]-2][section[1]-2]
            elif section[0]-1==0:
                result = dp[section[2]-1][section[3]-1]-dp[section[2]-1][section[1]-2]
            elif section[1]-1==0:
                result=dp[section[2]-1][section[3]-1]-dp[section[0]-2][section[3]-1]
        else: #(1,1)부터(x2,y2)
            result = dp[section[2] - 1][section[3] - 1]

        print(result)