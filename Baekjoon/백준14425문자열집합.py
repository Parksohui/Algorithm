import sys

if __name__=='__main__' :
    N,M=map(int, sys.stdin.readline().split())

    S=[]
    for i in range(N): #집합 S에 포함되어 있는 문자열
        S.append(sys.stdin.readline().strip())

    cnt=0
    for i in range(M): #검사해야 하는 문자열
        x=sys.stdin.readline().strip()

        if x in S: #집합 S에 포함되어 있으면
            cnt+=1

    print(cnt)
