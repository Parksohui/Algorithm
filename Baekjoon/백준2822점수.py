if __name__=='__main__':
    arr=[]
    arr2=[]
    for i in range(8): #입력
        a=int(input())
        arr.append(a)
        arr2.append(a)

    arr.sort(reverse=True) #정렬

    sum=0
    for i in range(5): #가장 점수 높은 5개의 합
        sum+=arr[i]
    print(sum)

    result=[]
    for i in range(5): #문제 번호
        result.append(arr2.index(arr[i])+1)

    result.sort()

    for i in range(5):
        print(result[i],end=' ')