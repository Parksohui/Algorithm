import heapq

def solution(operations):
    result = []

    for i in operations:
        x = i.split()

        if x[0] == "I":  # 숫자 삽입
            heapq.heappush(result, int(x[1]))
        elif x[0] == "D":
            if x[1] == "-1":  # 최솟값 삭제
                if len(result) != 0:
                    heapq.heappop(result)
            else:  # 최댓값 삭제
                temp = []
                for j in result:  # 최대 힙 만들기
                    heapq.heappush(temp, -int(j))
                if len(temp) != 0:  # 비어있지 않으면 삭제
                    heapq.heappop(temp)
                result = []
                for j in temp:  # 원래대로
                    heapq.heappush(result, -j)

    answer = []
    if len(result) == 0:  # 큐가 비어있으면
        answer = [0, 0]
    else:  # 비어있지 않으면
        k = heapq.heappop(result)  # 최솟값
        temp = []
        for j in result:  # 최대 힙
            heapq.heappush(temp, -j)
        answer.append(-heapq.heappop(temp))  # 최댓값
        answer.append(k)  # 최솟값

    return answer