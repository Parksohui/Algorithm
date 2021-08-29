import sys

if __name__=='__main__' :
    x=sys.stdin.readline().strip()

    check="UCPC"

    j=0
    for i in x:
        if i==check[j]:
            j+=1
            if j>3: #UCPC 다 만들면
                break

    if j>3:
        print("I love UCPC")
    else:
        print("I hate UCPC")