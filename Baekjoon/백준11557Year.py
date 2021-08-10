if __name__ == '__main__' :
    T=int(input())

    for i in range(T):
        N=int(input())

        arr=[]
        for j in range(N):
            arr.append(input().split())
        arr.sort(key=lambda x:-int(x[1])) #소비량 기준 정렬
        print(arr[0][0]) #학교 이름 출력