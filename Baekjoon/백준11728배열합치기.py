if __name__=='__main__':
    a,b=map(int, input().split())

    arr=list(map(int, input().split()))
    arr2=list(map(int, input().split()))

    result=arr+arr2 #배열 합치기

    result.sort() #배열 정렬

    for i in result:
        print(i, end=' ')

