def solution(n):
    answer = 0

    temp = str(n)
    for i in range(len(temp)):
        answer += int(temp[i])

    return answer