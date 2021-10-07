import sys

if __name__=='__main__':
    n,m=map(int,sys.stdin.readline().split())

    dict={}
    for i in range(n):
        x=sys.stdin.readline().strip() # 단어 입력

        if len(x)>=m: # 길이가 m 이상인 단어들만 외움
            if x in dict: # 이미 있으면 value +1
                dict[x]+=1
            else: # 없으면 key,value 추가
                dict[x]=1
    
    # 정렬 기준) 자주 나오는 단어, 길이 길수록, 알파벳 사전 순
    dict=sorted(dict.items(),key=lambda x:(-x[1],-len(x[0]),x[0]))

    for i in dict: # 출력
        print(i[0])
