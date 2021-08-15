if __name__=='__main__' :
    search=input()
    N=int(input())

    cnt=0
    for i in range(N):
        st=input()
        if search in st: #포함되어 있으면
            cnt+=1
        elif search in st+st: #문자열의 시작과 끝이 연결되어 있으면
            cnt+=1

    print(cnt)