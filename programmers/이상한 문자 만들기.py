def solution(s):
    answer = ''
    temp = s.split(" ")
    print(temp)
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            if (j % 2 == 0):
                answer += temp[i][j].upper()
            else:
                answer += temp[i][j].lower()
        if (i != len(temp) - 1):
            answer += " "

    return answer