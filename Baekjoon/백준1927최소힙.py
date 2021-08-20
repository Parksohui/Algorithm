import heapq
import sys

if __name__=='__main__' :
    N=int(sys.stdin.readline().strip())

    heap=[]
    for i in range(N):
        x=int(sys.stdin.readline().strip())

        if x==0:
            if len(heap)==0: #배열이 비어있는 경우
                print(0)
            else: #가장 작은 값 출력 및 배열에서 제거
                print(heapq.heappop(heap))
        else:
            heapq.heappush(heap,x)