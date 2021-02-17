if __name__=='__main__' :
    x=int(input())

    result=1
    for i in range(2,x+1): #팩토리얼 값 구하기
        result*=i

    result=str(result)[::-1] #뒤집기

    count=0

    for i in range(len(result)): #0 개수 count
        if result[i]=='0':
            count+=1
        else:
            break

    print(count)