import sys

def gcd(a,b): #최대공약수
    if b==0:
        return a
    return gcd(b,a%b)

if __name__=='__main__':
    a,b=map(int, sys.stdin.readline().split())

    result=gcd(a,b)
    print('1'*result)