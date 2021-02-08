
if __name__=='__main__':
    x=list(map(int, input().split()))

    que=[i for i in range(1,x[0]+1)]
    result=[]

    while(len(que)>=x[1]):
        que=que[x[1]-1::]+que[:x[1]-1]
        result.append(que.pop(0))

    while(len(que)!=0):
        temp=(x[1]%len(que))-1
        que=que[temp::]+que[:temp]
        result.append(que.pop(0))

    result=result+que
    
    #출력
    print("<",end='')

    for i in range(len(result)-1):
        print(result[i],end='')
        print(",",end=' ')

    print(result[-1],end='')
    print(">")