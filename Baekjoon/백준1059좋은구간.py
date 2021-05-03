if __name__=='__main__':
    a=int(input())

    arr=list(map(int, input().split()))

    temp=int(input())

    arr.sort() #정렬

    if temp in arr: #집합 안에 있다면 0출력
        print(0)
    else:
        max,min=0,0

        for i in range(len(arr)): #범위 찾기
            if arr[i]>temp:
                max=arr[i]
                if i!=0:
                    min=arr[i-1]
                break

        count=0
        for i in range(min+1,max):
            for j in range(max-1,min,-1):
                 if i<=temp and j>=temp: #사이 값인 것만
                    if i!=j: #A,B 같지 않음 A<B 만족 위해서
                        count+=1
        print(count)