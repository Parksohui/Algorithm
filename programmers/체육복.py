def solution(n, lost, reserve):
    answer = 0
    temp = []
    for i in range(n):
        temp.append(1)
    for i in lost:
        temp[i - 1] = 0
    for i in reserve:
        temp[i - 1] += 1

    for i in range(len(temp)):
        if (temp[i] == 0):
            if (i != 0 or i != len(temp) - 1):
                if (temp[i - 1] == 2):
                    temp[i - 1] = 1
                    temp[i] = 1
                elif (temp[i + 1] == 2):
                    temp[i] = 1
                    temp[i + 1] = 1
            else:
                if (i == 0 and temp[i + 1] == 2):
                    temp[i] = 1
                    temp[i + 1] = 1
                elif (i == len(temp) - 1 and temp[i - 1] == 2):
                    temp[i] = 1
                    temp[i - 1] = 1
    for i in range(len(temp)):
        if (temp[i] > 0):
            answer += 1

    return answer