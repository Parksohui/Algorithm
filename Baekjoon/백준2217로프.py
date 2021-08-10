if __name__=='__main__' :
    N=int(input())

    arr=[]
    for i in range(N):
        arr.append(int(input()))

    arr.sort(reverse=True) #정렬
    
    #임의로 몇 개의 로프 골라서 사용 가능
    #중량이 큰 것 사용 -> 그 보다 중량 큰 로프만 골라서 사용 가능
    #중량이 작은 것 사용 -> 그 보다 중량 큰 로프 사용 가능
    #정렬)중량이 점점 작아질수록 로프 여러개 가능
    for i in range(N):
        arr[i]*=(i+1)

    print(max(arr))