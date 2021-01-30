
def gcd(a,b):
    while(b!=0):
        r = a % b
        a=b
        b=r
        if(b==1):
            return 1
    return a

if __name__ == '__main__' :
    x=input().split()

    result=int(x[1])-int(x[0])
    temp=int(x[1])

    gcdresult=gcd(result,temp)

    print(str(result//gcdresult) +" " +str(temp//gcdresult))

