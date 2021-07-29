if __name__=='__main__':
    N=int(input())
    arr=list(map(int, input().split()))

    flag=False
    temp="YES"
    if len(arr)==1: #길이가 1일때
        print("YES")
    else:
        for i in range(1,len(arr)):
            if flag==False:
                if arr[i]>arr[i-1]: #수열 증가
                    pass
                else:
                    flag=True
            else:
                if arr[i]<arr[i-1]: #수열 감소
                    pass
                else: #산 x
                    temp="NO"

    print(temp)

