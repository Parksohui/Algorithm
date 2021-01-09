def solution(s):
    answer = True

    temp = []
    for i in range(len(s)):
        if (s[i] == "("):  # ( 이면 list에 넣기
            temp.append(s[i])
        else:  # ) 이면
            if (len(temp) == 0):  # 길이가 0이면 올바르지 않은 괄호
                answer = False
                break
            else:  # pop
                temp.pop()

    if (len(temp) != 0):  # 길이가 0이 아니면 올바르지 않은 괄호
        answer = False

    return answer