
def gcd(a,b): #최대공약수
    while(b!=0):
        r=a%b
        a=b
        b=r
        if b==1:
            return 1

    return a

if __name__=='__main__':
    a,b=map(int,input().split(":"))

    result=gcd(a,b)

    print(str(int(a/result))+":"+str(int(b/result)))
