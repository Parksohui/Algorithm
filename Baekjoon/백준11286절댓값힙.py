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
            else: #절댓값이 가장 작은 값 출력 및 배열에서 제거
                print(heapq.heappop(heap)[1])
        else:
            heapq.heappush(heap,(abs(x),x)) #절댓값 기준으로 정렬