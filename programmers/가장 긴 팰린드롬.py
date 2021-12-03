def solution(s):
    answer = 1  # 문자열 길이 1

    for i in range(len(s) - 1):  # 모든 경우의 수 - 문자열
        for j in range(i, len(s)):
            temp = s[i:j + 1]
            if temp == temp[::-1]:  # 팰린드롬 확인
                if answer < len(temp):  # 가장 긴 길이
                    answer = len(temp)

    return answer