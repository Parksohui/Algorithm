if __name__=='__main__':
    arr=set()

    for i in range(1,10001): #생성자 만들기 d(n)=n+n의 각 자리수
        temp=i #n
        for j in str(i): #각 자리수 더하기
            temp+=int(j)
        arr.add(temp)

    arr2=set([i for i in range(1,10001)])

    result=list(arr2-arr) #차집합

    result.sort() #정렬

    for i in result: #출력
        print(i)
