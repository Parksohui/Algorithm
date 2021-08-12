if __name__=='__main__' :
    N=int(input())

    arr=[1]
    x=0
    while True:
        x += 6
        arr.append(arr[-1]+x)
        if arr[-1]>=N:
            break

    result=0
    for i in range(len(arr)):
        result += 1
        if N<=arr[i]:
            break

    print(result)



