def solution(dartResult):
    temp = []
    for i in range(len(dartResult)):
        x = dartResult[i]
        if (x.isdigit()):  # 숫자 판별
            if (x == "1" and dartResult[i + 1] == "0"):  # 10인 경우
                temp.append(10)
            elif (x == "0" and i != 0):
                if (dartResult[i - 1] == "1"):
                    pass
                else:  # 0인 경우
                    temp.append(0)
            else:
                temp.append(int(x))
        if (x == "S"):  # Single
            pass
        if (x == "D"):  # Double
            temp[-1] *= temp[-1]
        if (x == "T"):  # Triple
            temp[-1] *= temp[-1] * temp[-1]
        if (x == "*"):  # 스타상
            if (len(temp) > 1):
                temp[-2] *= 2
                temp[-1] *= 2
            else:  # 스타상 - 첫번째 기회
                temp[-1] *= 2
        if (x == "#"):  # 아차상
            temp[-1] *= -1

    return sum(temp)