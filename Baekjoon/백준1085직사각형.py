if __name__=='__main__':
    arr=list(map(int,input().split()))

    minx=arr[2]-arr[0]

    if arr[0]<minx:
        minx=arr[0]

    miny=arr[3]-arr[1]

    if arr[1]<miny:
        miny=arr[1]

    print(min(miny,minx))