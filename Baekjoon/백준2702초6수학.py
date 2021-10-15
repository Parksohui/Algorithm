def gcd(a,b):
    if b==0:
        return a
    return gcd(b, a%b)

if __name__=='__main__':
    T=int(input())

    for i in range(T):
        a,b=map(int,input().split())

        k=gcd(a,b)
        print(int(a*b/k), int(k))
