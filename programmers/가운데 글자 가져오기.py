def solution(s):
    answer = ''
    index = len(s) // 2
    if (len(s) % 2 == 0):  # 짝수이면

        answer += s[index - 1]
        answer += s[index]
    else:
        answer += s[index]

    return answer