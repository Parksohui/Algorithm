import heapq

def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)  # 기존 list를 힙으로 변환

    while scoville[0] < K:  # K보다 작을때만 반복
        if len(scoville) == 1:  # 길이가 1이면 더이상 만들 수 없음
            answer = -1
            break
        temp = heapq.heappop(scoville)
        temp2 = heapq.heappop(scoville)
        heapq.heappush(scoville, temp + temp2 * 2)
        answer += 1

    return answer