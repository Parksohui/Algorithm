def solution(n):
    temp = str(n)
    result = []
    for i in range(len(temp)):
        result.append(int(temp[i]))
    result.sort(reverse=True)

    answer = ""
    for i in range(len(result)):
        answer += str(result[i])

    return int(answer)