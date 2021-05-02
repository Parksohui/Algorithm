import sys
if __name__=='__main__':
    a,b=map(int,input().split())

    dic={} #딕셔너리 선언

    for i in range(a):
        x=sys.stdin.readline().split()

        dic[x[0]]=x[1] #딕셔너리 추가


    for i in range(b):
        x=sys.stdin.readline().strip() #strip->개행문자 제거
        print(dic.get(x))

