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
    a,b=input().split()

    a=int(a)
    b=int(b)

    print(gcd(a,b))
    print(lcm(a,b))

