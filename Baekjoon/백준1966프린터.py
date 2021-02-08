if __name__=='__main__':
    x=int(input())

    for i in range(x):
        temp=list(map(int,input().split()))
        priorities=list(map(int,input().split()))
        idx=[i for i in range(temp[0])]

        result=[]

        while(len(priorities)!=0):
            if (len(priorities) == 1):  # 길이가 1이면 바로 출력 가능
                result.append(idx[0])  # index 저장
                break
            x = priorities[0]
            y = idx[0]
            priorities = priorities[1:]
            idx = idx[1:]
            if (x < max(priorities)):  # 대기목록에 중요도 높은 문서가 한개라도 있다면
                priorities.append(x)  # 가장 마지막에 넣음
                idx.append(y)  # index도 가장 마지막으로 넣음
            else:  # 대기목록에 중요도 높은 문서가 없으면
                result.append(y)  # result list에 추가

        print(result.index(temp[1]) + 1)  # index의 위치를 결과로 반환

