import sys
if __name__=='__main__' :

    #PyPy3 통과

    NM=list(map(int,sys.stdin.readline().split()))
    arr=list(map(int,sys.stdin.readline().split()))

    cnt=0
    for i in range(NM[0]):
        sum=0
        for j in range(i,NM[0]):
            sum+=arr[j]
            if sum==NM[1]:
                cnt+=1
                break
            elif sum>NM[1]:
                break

    print(cnt)


    # ----------------------------------------------------------

    # Python3 통과

    cnt=0
    left=0
    right=left+1
    sum=arr[left]

    while left!=NM[0]:

        if sum<NM[1]:
            if right>=NM[0]:
                break
            sum+=arr[right]
            right+=1
        if sum == NM[1]:
            cnt+=1
            left+=1
            right=left+1
            if left==NM[0]:
                break
            sum=arr[left]
        if sum > NM[1]:
            left += 1
            right = left + 1
            if left==NM[0]:
                break
            sum = arr[left]

    print(cnt)
