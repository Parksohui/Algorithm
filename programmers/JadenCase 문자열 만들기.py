def solution(s):
    answer = ''
    temp = s.split()  # 공백 기준 분리

    for i in range(len(temp)):
        word = ""
        word += temp[i][0].upper()  # 첫 문자만 대문자
        for j in range(1, len(temp[i])):  # 나머지는 소문자
            word += temp[i][j].lower()
        answer += word
    result = list(answer)

    for i in range(len(s)):  # 원래 문자열과 같이 공백 추가
        if (s[i] == " "):
            result.insert(i, " ")

    answer = ''
    for i in range(len(result)):  # list -> str
        answer += result[i]

    return answer