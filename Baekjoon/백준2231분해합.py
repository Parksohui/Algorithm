if __name__=='__main__' :
    N=int(input())
    result=-1

    for i in range(N):
        sum = 0
        sum+=i
        i=str(i)
        for j in range(len(i)):
            sum+=int(i[j])

        if sum==N:
            result=int(i)
            break

    if result==-1:
        result=0
    print(result)
