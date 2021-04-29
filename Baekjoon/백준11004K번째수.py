import sys
if __name__=='__main__' :
    a,b=map(int,sys.stdin.readline().split())

    arr=list(map(int,sys.stdin.readline().split()))

    arr.sort()

    print(arr[b-1])