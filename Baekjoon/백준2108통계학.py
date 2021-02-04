if __name__=='__main__' :
    x=int(input())

    result=[]
    for i in range(x):
        result.append(int(input()))

    print(round(sum(result)/x)) #산술평균

    result.sort()

    print(result[x//2]) #중앙값

    maxnumber=[result[0]]
    maxcount=result.count(result[0])

    for i in range(1,len(result)):
        count=result.count(result[i])

        if maxcount < count:
            maxnumber=[result[i]]
            maxcount=count
        elif maxcount==count:
            maxnumber.append(result[i])

    maxnumber=list(set(maxnumber))
    if len(maxnumber)!=1:
        maxnumber.sort()
        print(maxnumber[1])
    else:
        print(maxnumber[0]) #최빈값

    print(max(result)-min(result)) #범위
