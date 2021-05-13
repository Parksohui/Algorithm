if __name__=='__main__':
    M=int(input())
    N=int(input())

    arr=[]
    for i in range(M,N+1): #소수찾기
        if i==2: #2는 소수
            arr.append(i)
        for j in range(2,i): 
            if i%j==0: #나눠지는 것이 있으면 소수가 아님
                break
            if j==i-1: #나눠지는 것이 없으면 소수
                arr.append(i)

    if len(arr)==0: #소수가 없는 경우
        print(-1)
    else: #소수 있는 경우-합, 최솟값 출력
        print(sum(arr))
        print(min(arr))