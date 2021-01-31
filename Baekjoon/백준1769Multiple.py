if __name__=='__main__' :
    x=list(map(int,input()))
    count=0

    while(len(x)!=1):
        count+=1
        temp=str(sum(x))
        x=list(map(int,temp))

    result="YES"
    if x[0]%3 !=0:
        result="NO"

    print(count)
    print(result)