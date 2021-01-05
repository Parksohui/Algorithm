def solution(number, k):
    answer = ''
    result = []

    for i in range(len(number)):
        while result and result[-1] < number[i] and k > 0:  # result길이가 0보 큼 and 마지막 값<넣을 값 and k>0
            result.pop()  # list에서 제거
            k -= 1  # k-1
        result.append(number[i])  # 값 추가
        if (k == 0):  # k가 0이면 제거할 수 없음
            result += number[i + 1:]  # 뒤에 부분 넣어줌
            break
    if (len(number) - k < len(result)):  # 원하는 수 만큼 제거를 덜했으면 (같은 수 일 경우)
        for i in range(len(result) - len(number) + k):  # 원하는수 만큼 빼줌
            result.pop()

    for i in result:
        answer += i

    return answer