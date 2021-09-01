import sys
from itertools import product # 중복 순열

if __name__=='__main__':
    N,M=map(int, sys.stdin.readline().split())

    nums=[i+1 for i in range(N)]

    for i in product(nums,repeat=M):
        print(' '.join(map(str,i))) #int tuple -> string