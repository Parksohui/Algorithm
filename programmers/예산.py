def solution(d, budget):
    answer = 0

    d.sort()  # 정렬
    for i in d:
        if ((budget - i) >= 0):  # 예산 남아있때까지 지원 가능
            budget -= i
            answer += 1

    return answer