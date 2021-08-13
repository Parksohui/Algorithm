if __name__=='__main__' :
    n=int(input())

    arr=[1,1,2,5]

    for j in range(4,36): #범위 0<=n<=35
        sum=0
        for i in range(j): #점화식
            sum+=arr[i]*arr[j-(i+1)]
        arr.append(sum)

    print(arr[n])


