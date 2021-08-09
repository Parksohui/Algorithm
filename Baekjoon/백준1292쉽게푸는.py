if __name__=='__main__':
    a,b=input().split()

    sum=0
    i=1

    arr=[]
    while True:
        sum+=i
        i+=1

        if sum>=int(a):
            arr.append(i-1)
            arr.append(sum-int(a)+1)
            break

    while True:
        sum += i
        i += 1

        if sum>=int(b):
            arr.append(i-1)
            arr.append(int(b)-sum+i-1)
            break

    result=arr[0]*arr[1]+arr[2]*arr[3]
    for i in range(arr[0]+1,arr[2]):
        result+=i*i


    print(result)

