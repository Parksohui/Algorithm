def solution(n, lost, reserve):
    answer = 0
    temp = []
    for i in range(n):  # 1로 setting
        temp.append(1)
    for i in lost:  # 도난당한 학생들
        temp[i - 1] -= 1
    for i in reserve:  # 여벌의 체육복 가져온 학생들
        temp[i - 1] += 1

    for i in range(len(temp)):
        if (temp[i] == 0):  # 체육복이 없으면
            if (i != 0 and i < len(temp) - 1):  # 양 끝 학생이 아니면
                if (temp[i - 1] == 2):  # 앞사람이 2개면 빌림
                    temp[i - 1] = 1
                    temp[i] = 1
                elif (temp[i + 1] == 2):  # 뒷사람이 2개면 빌림
                    temp[i] = 1
                    temp[i + 1] = 1
            else:  # 양 끝 학생이면
                if (i == 0 and temp[i + 1] == 2):  # 맨 앞 사람 & 뒷사람이 여별을 가지고 있으면
                    temp[i] = 1
                    temp[i + 1] = 1
                elif (i == len(temp) - 1 and temp[i - 1] == 2):  # 맨 뒷사람 & 앞사람이 여벌을 가지고 있으면
                    temp[i] = 1
                    temp[i - 1] = 1
    for i in range(len(temp)):  # 체육수업 들을 수 있는 학생 count
        if (temp[i] > 0):
            answer += 1

    return answer