import sys

if __name__=='__main__':
    k,l=map(int, sys.stdin.readline().split())

    dic={}

    for i in range(l): # 입력_중복으로 들어오면 뒤에 들어온 번호로 입력
        x=sys.stdin.readline().strip()
        dic[x]=i

    dic=sorted(dic.items(), key=lambda x:x[1]) # 번호 순으로 정렬

    cnt=0
    for i in dic:
        print(i[0])
        cnt+=1
        if cnt==k: #수강 가능 인원 check
            break