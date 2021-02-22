import sys
from collections import  Counter

if __name__=='__main__' :
    x=int(sys.stdin.readline().strip())

    result=[]
    for i in range(x):
        result.append(int(sys.stdin.readline().strip()))

    print(round(sum(result)/x)) #산술평균

    result.sort()

    print(result[x//2]) #중앙값

    # 데이터 개수가 많은 순으로 정렬된 배열을 반환
    mostvalue=Counter(result).most_common()
    value=0 #최빈값

    if len(mostvalue)>1: #list 길이가 1보다 클때
        if mostvalue[0][1]==mostvalue[1][1]: #최빈값이 여러개라면
            value=mostvalue[1][0] #두 번째로 작은 값 출력
        else: #최빈값이 한개라면
            value=mostvalue[0][0]
    else:
        value=mostvalue[0][0]

    print(value) #최빈값 출력

    print(max(result)-min(result)) #범위
