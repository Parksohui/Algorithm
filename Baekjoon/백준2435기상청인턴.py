if __name__=='__main__' :
    x=list(map(int,input().split()))

    value=list(map(int, input().split()))

    result=[]
    for i in range(x[0]-x[1]+1): #연속적인 날짜 수 만큼 합 구하기
        result.append(sum(value[i:i+x[1]]))

    print(max(result)) #최대가 되는 값 출력