if __name__=='__main__':

    n=list(map(int,input().split()))

    x = [0, 1]
    num = 0
    i = 2

    while n[1]!=0: #b가 0이 아닐때 반복
        x.append(x[i-2]+x[i-1]) #피보나치
        i+=1
        if n[0]<=x[-1] and n[1]>=x[-1]: #구간 포함되는 피보나치 수
            num+=1
        elif n[1]<x[-1]: #구간 벗어나면 새로 입력
            print(num)
            x = [0, 1]
            num = 0
            i = 2
            n = list(map(int, input().split()))

