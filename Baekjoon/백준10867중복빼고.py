if __name__=='__main__' :
    x=int(input())

    temp=list(map(int,input().split()))

    temp=list(set(temp))  #중복 제거

    temp.sort() #오름차순 정렬

    for i in range(len(temp)-1): #출력
        print(temp[i],end=' ')

    print(temp[-1])