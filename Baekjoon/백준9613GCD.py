from itertools import combinations #조합

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

if __name__=='__main__' :
    t=int(input()) #case 수

    for i in range(t):
        arr=list(map(int,input().split()))

        pair=list(combinations(arr[1:],2)) #수의 개수 제외한 조합
        sum=0

        for j in pair:
            sum+=gcd(j[0],j[1])
        print(sum)