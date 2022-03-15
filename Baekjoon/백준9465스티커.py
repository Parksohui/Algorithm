import sys

if __name__ =='__main__':
    T=int(input()) # 테스트 케이스

    for i in range(T):
        arr = [] # 스티커 점수
        n=int(input())
        arr.append(list(map(int, sys.stdin.readline().split())))
        arr.append(list(map(int, sys.stdin.readline().split())))

        dp=[[arr[0][0]],[arr[1][0]]]
        for j in range(1,n):
            if j==1:
                dp[0].append(dp[1][0]+arr[0][j])
                dp[1].append(dp[0][0]+arr[1][j])
            else:
                dp[0].append(max(arr[0][j]+dp[1][j-1], arr[0][j]+dp[1][j-2]))
                dp[1].append(max(arr[1][j]+dp[0][j-1], arr[1][j]+dp[0][j-2]))
        if dp[0][-1]>=dp[1][-1]: # 최댓값 출력
            print(dp[0][-1])
        else:
            print(dp[1][-1])