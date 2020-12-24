def solution(s, n):
    answer = ''
    for i in range(len(s)):
        temp = ord(s[i]) + n
        if (ord(s[i]) == 32):
            answer += " "
        elif (ord(s[i]) <= 90 and temp > 90):
            temp = 65 + (temp - 91)
            answer += chr(temp)
        elif (ord(s[i]) <= 122 and temp > 122):
            temp = 97 + (temp - 123)
            answer += chr(temp)
        else:
            answer += chr(temp)

    return answer