if __name__ == '__main__' :
    T=int(input())

    case=[]
    for i in range(T): # 테스트 케이스
        case.append(int(input()))

    dp=[1,2,4]
    for i in range(3,max(case)):
        dp.append((dp[i-1]+dp[i-2]+dp[i-3])%1000000009)

    for i in case:
        print(dp[i-1])