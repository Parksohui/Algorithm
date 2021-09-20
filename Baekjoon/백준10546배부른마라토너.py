import sys

if __name__=='__main__':
    n=int(input())

    dic={}
    for i in range(n): # 참가자
        x=sys.stdin.readline()
        if x in dic:
            dic[x]+=1
        else:
            dic[x]=1

    for i in range(n-1): # 완주한 사람
        x=sys.stdin.readline()
        dic[x]-=1

    for item in dic.items(): # 완주 못한 참가자
        if item[1]!=0:
            print(item[0])
