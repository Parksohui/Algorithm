if __name__=='__main__':
    a,b=map(int,input().split())

    arr=[i for i in range(1,a+1)]

    result=[]
    idx=0
    while len(arr)!=0:
        if len(arr)==0: #제거 완료
            break
        idx+=b-1 #idx 구하기
        if idx>=len(arr): #리스트 길이 벗어나면
            idx=idx%len(arr)
        result.append(arr.pop(idx)) #pop

    #출력
    print("<",end='')
    for i in range(a):
        print(str(result[i]), end='')
        if i!=a-1:
            print(", ", end='')
    print(">")