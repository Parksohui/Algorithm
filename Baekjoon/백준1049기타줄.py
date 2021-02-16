if __name__=='__main__' :
    x=list(map(int, input().split())) #N,M 입력

    bundle=[]
    piece=[]

    for i in range(x[1]): #브랜드의 패키지 가격과 낱개 가격 입력
        a,b=input().split()
        bundle.append(int(a))
        piece.append(int(b))

    #정렬
    bundle.sort()
    piece.sort()

    money=0

    while(x[0]>0):
        if x[0]<=6: #6개 이하일때 낱개, 묶음 중 최솟값
            if bundle[0] <=piece[0]*x[0]:
                money+=bundle[0]
            else:
                money+=piece[0] * x[0]
            x[0]-=x[0]
            
        else: #6개보다 많을때
            if bundle[0] <=piece[0]*6: #묶음이 더 최솟값이라면
                money+=bundle[0]
            else: #낱개가 더 최솟값이라면
                money+=piece[0] * 6
            x[0] -= 6

    print(money)


