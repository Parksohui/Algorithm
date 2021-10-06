import sys
from itertools import combinations_with_replacement # 중복 조합

if __name__=='__main__':
    n=int(sys.stdin.readline().strip())

    num=[1,5,10,50]
    arr=set() # 서로 다른 수 만들기 위해 set 선언

    for i in combinations_with_replacement(num, n):
        arr.add(sum(list(i)))

    print(len(arr)) # 길이 출력

