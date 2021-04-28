def solution(n, times):
    left, right = 1, max(times) * n  # left를 제일 작은 값, right를 가장 최댓값으로 선언
    answer = 0

    while left <= right:
        mid = (left + right) // 2  # 중간값을 찾음
        people = 0  # 사람 수

        for i in times:
            people += mid // i  # 각 시간마다 몇명의 사람을 심사할 수 있는지
            if people >= n:  # 다 심사할수 있으면
                break

        if people < n:  # 다 심사못하면
            left = mid + 1  # left값을 늘려줌
        else:
            answer = mid
            right = mid - 1  # right 값을 줄여줌

    return answer