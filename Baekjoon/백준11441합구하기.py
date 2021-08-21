import sys

if __name__=='__main__' :
    N=int(sys.stdin.readline().strip()) #개수
    arr=list(map(int,sys.stdin.readline().split())) #배열

    M=int(sys.stdin.readline().strip()) #구간 개수

    dp=[arr[0]]
    for i in range(1,N): #앞에서부터의 구간 합
        dp.append(dp[-1]+arr[i])

    for i in range(M):
        section=list(map(int,sys.stdin.readline().split())) #구간

        result=0
        if section[0]-2>=0: #구간에 포함되지 않는 값 제거
            result=dp[section[1]-1]-dp[section[0]-2]
        else: 
            result=dp[section[1]-1]

        print(result)