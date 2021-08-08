from itertools import combinations

if __name__=='__main__' :
    N=list(map(int,input().split()))

    card=list(map(int,input().split()))

    arr=list(combinations(card,3)) #조합

    max=0
    for i in range(len(arr)):
        if N[1]>=sum(arr[i]): #합이 M을 넘지 않으면
            if max<sum(arr[i]): #M과 최대한 가까운 수
                max=sum(arr[i])

    print(max)