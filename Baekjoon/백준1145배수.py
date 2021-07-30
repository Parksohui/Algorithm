from itertools import combinations

def GCD(a,b): #최대공약수
    if b==0:
        return a
    return GCD(b, a%b)

def LCM(a,b,c): #최소공배수
    k=a*b/GCD(a,b)
    return k*c/GCD(k,c)

if __name__=='__main__':
    arr=list(map(int, input().split()))

    arrlist=list(combinations(arr,3)) #조합

    result=[]
    for i in arrlist:
        result.append(LCM(i[0],i[1],i[2]))

    print(int(min(result))) #가장 작은 수


