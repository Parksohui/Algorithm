import sys

if __name__=='__main__':
    n,k=map(int,sys.stdin.readline().split())

    a=1
    b=1

    # 이항 계수 = n!/k!(n-k)!
    for i in range(k+1,n+1):
        a*=i

    for i in range(1, n-k+1):
        b*=i

    print((a//b)%10007) # 10007로 나눈 나머지

