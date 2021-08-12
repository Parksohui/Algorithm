if __name__=='__main__' :
    NK=list(map(int,input().split()))

    arr=[]
    for i in range(2,NK[0]+1): #2부터 N까지 모든 정수를 적는다
        arr.append(i)

    cnt=0
    result={}
    j=0
    while cnt<=NK[1]:
        if len(result)>=NK[1]:
            break
        for i in arr: #P의 배수를 크기 순서대로 지운다
            if i%arr[j]==0:
                result[i]=i
        j+=1

    print(list(result.values())[NK[1]-1]) #dict->list index 접근



