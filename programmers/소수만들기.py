from itertools import combinations  # 조합(순서x)


def solution(nums):
    answer = 0

    arr = list(combinations(nums, 3))  # 조합 구하기(순서 상관 x)

    for i in arr:
        temp = sum(i)  # 합
        count = 0
        for j in range(2, temp):
            if temp % j == 0:  # 소수가 아니면
                break
            if j == temp - 1:  # 소수라면
                answer += 1

    return answer