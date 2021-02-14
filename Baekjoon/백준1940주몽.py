if __name__=='__main__' :
    x=int(input()) #재료의 개수
    y=int(input()) #갑옷 만드는데 필요한 수

    temp=list(map(int,input().split())) #재료들의 고유한 번호

    temp.sort()

    result=0 #개수

    i=0
    j=len(temp)-1

    while(i<j): #i>=j이면 종료조건
        k = temp[i] + temp[j] #합
        if k<y: #합이 필요한 수보다 작으면 값을 키워야함
            i+=1
        elif k>y: #합이 필요한 수보다 크면 값을 줄여야함
            j-=1
        else: #합과 필요한 수가 같으면
            result+=1
            temp.pop(i) #재료 제거
            temp.pop(j-1) #재료 제거
            i=0 #index 초기화
            j=len(temp)-1

    print(result)








