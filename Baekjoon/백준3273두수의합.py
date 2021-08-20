import sys
if __name__=='__main__' :
    n=int(sys.stdin.readline().strip()) #개수

    arr=list(map(int,sys.stdin.readline().split())) #수열

    x=int(sys.stdin.readline().strip()) #합의 값

    arr.sort() #정렬

    left,right=0,n-1
    cnt=0

    while left<right:
        sum=arr[left]+arr[right] #두 수의 합

        if sum==x: #같으면 cnt+1, 왼쪽 idx+1
            cnt+=1
            left+=1
        if sum>x: #크면 오른쪽 idx-1
            right-=1
        if sum<x: #작으면 왼족 idx+1
            left+=1
    print(cnt)

