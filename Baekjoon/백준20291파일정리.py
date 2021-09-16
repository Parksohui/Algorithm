import sys

if __name__=='__main__' :
    n=int(input())

    dic={}
    for i in range(n):
        x=sys.stdin.readline().strip().split(".") # 확장자 분리

        if x[1] not in dic: # dict에 key값으로 없으면
            dic[x[1]]=1
        else: # dict에 key값이 있으면 vlaue 증가
            dic[x[1]]+=1

    answer=sorted(dic.items()) # key순 정렬

    for i in answer: # 출력
        print(' '.join(map(str,i)))