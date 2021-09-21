import sys

if __name__=='__main__':
    n,c=map(int,sys.stdin.readline().split())

    arr=list(map(int, sys.stdin.readline().split()))
    dict={}
    for i in arr: # 빈도 확인
        if i not in dict:
            dict[i]=1
        else:
            dict[i]+=1

    dict=sorted(dict.items(), key=lambda  x:x[1], reverse=True) # 빈도 정렬

    for i in dict: # 출력
        print((str(i[0])+' ') *i[1], end='')