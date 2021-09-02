import sys

if __name__=='__main__':
    n=int(sys.stdin.readline().strip())

    arr=[1,1,1] # f(1) = f(2) = f(3) = 1

    if n>3:
        for i in range(3,n): # f(n) = f(n-1) + f(n-3)
            arr.append(arr[i-1]+arr[i-3])

    print(arr[n-1])