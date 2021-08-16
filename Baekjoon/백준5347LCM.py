#LCM 최소 공배수는 a*b/gcd(a,b)

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)


if __name__=='__main__' :
    n=int(input())

    for i in range(n):
        arr=list(map(int,input().split()))

        print(int(arr[0]*arr[1]/gcd(arr[0],arr[1])))