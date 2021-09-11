if __name__=='__main__' :
    T=int(input()) # 테스트 케이스

    for i in range(T):
        x=input().split() # 공백 기준 분리
        for j in range(len(x)):
            x[j]=x[j][::-1] # 뒤집기
        print(' '.join(x)) # 이어서 출력
