import sys
if __name__=='__main__':

    a,b=map(int, sys.stdin.readline().split())

    arr=set(map(int, sys.stdin.readline().split()))

    arr2=set(map(int, sys.stdin.readline().split()))

    cnt=[0 for i in range(a)]

    arr=list(arr-arr2) #set을 활용하여 차집합 구한 후 list로 변환

    if len(arr)==0:
        print(0)
    else:
        arr.sort()
        print(len(arr))
        for i in arr:
            print(i, end=' ')


