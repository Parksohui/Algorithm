if __name__ == '__main__' :
    x=input().split()

    result=[]
    for i in range(1,int(x[0])+1): #약수 구하기
        if int(x[0]) % i ==0:
            result.append(i)

    answer=0
    if len(result)>=int(x[1]): #K번째 작은 수
        result.sort()
        answer=result[int(x[1])-1]

    print(answer)
