import sys

def gcd(a,b): #최대공약수
    while(b!=0):
        r = a % b
        a=b
        b=r
        if(b==1):
            return 1
    return a

def lcm(a,b): #최소공배수
    return a*b//gcd(a,b)

if __name__=='__main__' :
    A,B=map(int, sys.stdin.readline().split())
    C,D=map(int, sys.stdin.readline().split())

    deno=lcm(B,D) #분모_최소공배수
    num=int(A*(deno/B)+C*(deno/D)) #분자

    mea=gcd(num,deno) #최대공약수 찾기

    print(int(num/mea), int(deno/mea)) #기약분수=최대 공약수로 나눈 값


