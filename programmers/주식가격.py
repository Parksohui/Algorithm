def solution(prices):
    answer = []

    for i in range(len(prices)):
        count = 0
        for j in range(i + 1, len(prices)):
            if (prices[i] > prices[j]):  # 현재보다 작은 값이 있다면
                answer.append(j - i)  # 초 저장
                break
            else:
                count += 1
        if (count == len(prices) - 1 - i):  # 끝까지 가격이 떨어지지 않았다면
            answer.append(len(prices) - 1 - i)  # 초 저장

    return answer