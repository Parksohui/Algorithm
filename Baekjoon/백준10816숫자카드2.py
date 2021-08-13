import sys

if __name__=='__main__' :
    N=int(sys.stdin.readline().strip())
    arr=list(map(int, sys.stdin.readline().split()))

    M=int(sys.stdin.readline().strip())
    arr2 = list(map(int, sys.stdin.readline().split()))

    dict={}
    for i in arr: #dict key, value로 값 추가
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1

    for i in arr2: 
        if i in dict: #dict에 있으면 value 출력
            print(dict[i],end=' ')
        else: #dict에 없으면 0 출력
            print(0, end=' ')

