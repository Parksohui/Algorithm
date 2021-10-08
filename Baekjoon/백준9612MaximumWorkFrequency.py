import sys

if __name__=='__main__':
    n=int(input())

    dict={}
    for i in range(n):
        x=sys.stdin.readline().strip() # 입력
        if x in dict: # key 있으면 value+1
            dict[x]+=1
        else: # key 없으면 key, value 추가
            dict[x]=1

    dict=sorted(dict.items(), key=lambda x:-x[1]) # 단어 많이 나온 순으로 정렬

    arr=[]
    maxnum=dict[0][1]
    for i in dict: # 최대 빈도수 뽑기
        if i[1]==maxnum:
            arr.append([i[0],i[1]])
        else:
            break

    arr.sort(key=lambda x:x[0], reverse=True) # 2 이상일 경우 사전순에서 나중에 오는 것
    print(' '.join(map(str,arr[0])))

