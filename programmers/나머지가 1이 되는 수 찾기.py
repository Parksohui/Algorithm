def solution(n):
    answer = 0

    for i in range(1, n):
        if n % i == 1:  # 나머지가 1되는 수
            answer = i
            break

    return answer