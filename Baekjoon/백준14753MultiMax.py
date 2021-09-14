if __name__=='__main__' :
    x=int(input())

    arr=list(map(int,input().split()))
    arr.sort(reverse=True) #내림차순 정렬

    answer=1
    for i in range(3):
        if i==2 and arr[i]<=0: #3번째 값이 음수이면 x
            break
        else: # 양수일 경우 곱
            answer*=arr[i]

    arr=arr[::-1] #뒤집기
    temp=1
    for i in range(2): # 음수 2개 곱하기
        temp*=arr[i]
    if arr[-1]>0: # 맨 마지막이 양수이면 곱하기
        temp*=arr[-1]

    if answer>=temp: # 양수*양수*(양수) or 음수*음수*(양수)
        print(answer)
    else:
        print(temp)
