if __name__=='__main__' :
    arr=list(map(int,input().split()))

    # arr[2]*x > arr[0]+(arr[1]*x)
    if arr[2]-arr[1]<1:
        print(-1)
    else:
        x=arr[0]/(arr[2]-arr[1])

        print(int(x+1))
