if __name__=='__main__' :
    x=list(map(int,input().split()))

    value=list(map(int, input().split()))

    temp=sum(value[0:x[1]]) #처음 연속적인 날짜 수 만큼 합 구함

    maxvalue=temp


    for i in range(1,x[0]-x[1]+1): #연속적인 날짜 수 만큼 합 구하기
       #처음에 0~N-1까지 구한 다음 수열의 합은 1~N 이므로
       #앞에서 구한 값에 0을 빼고 N을 더하면 되는 것을 이용
       temp-=value[i-1]
       temp+=value[i+x[1]-1]

       if maxvalue<temp:
           maxvalue=temp

    print(maxvalue) #최대가 되는 값 출력