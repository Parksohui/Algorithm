if __name__=='__main__' :
    x=int(input()) #학생 수

    temp=[]
    for i in range(x):
        y=input()
        temp.append(y[::-1]) #뒤집어서 list 추가

    bool=True
    idx=1

    while(bool):
        result=[]
        cnt=0
        for i in range(x): #slicing 해서 list 추가
            result.append(int(temp[i][:idx]))

        for i in range(x): #서로 다른 번호인지 확인
            if result.count(result[i])>1: #같은 번호가 있다면
                idx+=1
                break
            else: #같은 번호가 없다면
                cnt+=1

        if cnt==x: #서로 다르다면
            bool=False

    print(idx)
