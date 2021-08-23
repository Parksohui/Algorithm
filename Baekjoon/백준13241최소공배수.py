def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

if __name__=='__main__' :

    A,B=map(int, input().split())

    print(int(A*B/gcd(A,B)))