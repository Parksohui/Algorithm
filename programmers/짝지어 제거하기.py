def solution(s):
    answer = 1

    temp = []

    temp.append(s[0])  # 첫번째 값 추가
    for i in range(1, len(s)):
        if (len(temp) == 0):  # 길이가 0이면 그냥 추가
            temp.append(s[i])
        elif (temp[-1] == s[i]):  # 같은 값이면 pop
            temp.pop()
        else:  # 같은 값이 아니면 추가
            temp.append(s[i])
    if (len(temp) != 0):  # 길이가 0이 아니면 짝지어 제거하기 성공 x
        answer = 0

    return answer