if __name__=='__main__' :
    N=int(input()) #사람 수

    num=[]
    for i in range(N):
        num.append(list(map(int,input().split())))

    #전체 비교하며 자신보다 덩치 큰 사람이 있을 경우 score+=1
    for i in num:
        score=1
        for j in num:
            if i[0]<j[0] and i[1]<j[1]:
                score+=1
        print(score, end=' ')
