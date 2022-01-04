import sys

if __name__=='__main__':

    t=int(sys.stdin.readline())

    for i in range(t):
        n,m=map(int, sys.stdin.readline().split())
        a=list(map(int, sys.stdin.readline().split()))
        b=list(map(int, sys.stdin.readline().split()))
        
        #정렬
        a.sort(reverse=True)
        b.sort(reverse=True)

        result=0
        idx=0
        for j in a: # A list
            while True:
                if idx >= m: # index 종료 조건
                    break
                if j>b[idx]: # 크면 -> 나머지 값보다도 다 큼
                    result+=(m-idx)
                    break
                idx+=1
        print(result)
