if __name__=='__main__':
    a,b=input().split()

    a=a[::-1]
    b=b[::-1]

    if (len(a) > len(b)):
        indextemp = len(a) - len(b)
        for i in range(indextemp):
            b += '0'
    else:
        indextemp = len(b) - len(a)
        for i in range(indextemp):
            a += '0'

    result=[]
    next = 0
    for i in range(len(a)):
        temp=int(a[i])+int(b[i])+next
        next = 0
        if(temp>1):
            next=1
            temp=temp-2.
        result.append(temp)
    if(next==1):
        result.append(next)
    result.reverse()

    if(len(result)!=1 and result[0]==0):
        del result[0]

    answer=''
    for i in range(len(result)):
        answer+=str(result[i])



    print(answer)