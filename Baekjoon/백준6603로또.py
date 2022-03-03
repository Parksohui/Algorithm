import sys
from itertools import combinations #조합

if __name__=='__main__':
    while True:
        a=list(sys.stdin.readline().split())
        if a[0]=='0': # 종료 조건
            break
        else: #k=a[0], s=a[1::]
            s=a[1::]
            arr=list(combinations(s,6))
            for i in arr:
                print(' '.join(i))
            print()