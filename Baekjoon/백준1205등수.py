if __name__=='__main__' :
    x=list(map(int,input().split()))

    if x[0]!=0: #N이 0보다 큰 경우엠나 주어짐
        score=list(map(int,input().split()))
    else: #N이 0일때 빈 리스트
        score=[]

    result = 0

    if len(score)!=0:
        score=score[:x[2]]
        if len(score)==x[2] and score[-1]>=x[1]: #점수가 랭킹 리스트에 올라갈 수 없으면
            result=-1
        else: #랭킹 리스트에 올라가면
            score.append(x[1])
            score.sort(reverse=True)
            result=score.index(x[1])+1
    else: #랭킹 리스트에 처음 추가하는 경우
        result=1

    print(result)