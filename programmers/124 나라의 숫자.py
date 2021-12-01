def solution(n):
    answer = ''
    arr = ['4', '1', '2']

    while True:
        answer += arr[n % 3]  # 나머지 idx에 해당하는 값
        if n % 3 == 0:  # 3으로 나누어떨어지면 -1
            n = n // 3 - 1
        else:
            n = n // 3
        if n == 0:  # 종료 조건
            break

    answer = answer[::-1]  # 뒤집기
    return answer