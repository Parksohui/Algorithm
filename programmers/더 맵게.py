def solution(scoville, K):
    answer = 0

    scoville.sort()  # 정렬
    while scoville[0] < K:
        if (len(scoville) == 1):  # 길이가 1이면 K이상으로 만들기 불가
            answer = -1
            break
        temp = scoville.pop(0)  # 가장 맵지 않은 음식의 스코빌 지수
        temp2 = scoville.pop(0)  # 두 번째로 맵지 않은 음식의 스코빌 지수
        scoville.append(temp + (temp2 * 2))
        scoville.sort()  # 정렬
        answer += 1  # 섞어야 하는 횟수 +1

    return answer