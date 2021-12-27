import sys

if __name__=='__main__':
    N,M=map(int, sys.stdin.readline().strip().split())

    temp=[]
    for i in range(N):
        temp.append(sys.stdin.readline().strip()) # 문자열 입력

    find=[]
    for i in range(M):
        find.append(sys.stdin.readline().strip()) # 접두사 입력

    #정렬
    find.sort()
    temp.sort()

    cnt=0
    s=0
    for i in find:
        for j in range(s,N):
            if i==temp[j][:len(i)]:
                cnt+=1
                s=j # 정렬 했기 때문에 index 교체
                break

    print(cnt)



