import sys
from itertools import permutations # 순열(순서 o)

if __name__=='__main__':
    N,M=map(int, sys.stdin.readline().split())

    nums=[i+1 for i in range(N)]
    arr=list(permutations(nums, M))

    for i in arr:
        print(' '.join(map(str,i))) #int tuple -> string