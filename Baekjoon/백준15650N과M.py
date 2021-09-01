import sys
from itertools import combinations  # 조합(순서x)

if __name__=='__main__':
    N,M=map(int, sys.stdin.readline().split())

    nums=[i+1 for i in range(N)]
    arr=list(combinations(nums, M))

    for i in arr:
        print(' '.join(map(str,i))) #int tuple -> string