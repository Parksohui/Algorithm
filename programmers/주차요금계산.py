def solution(fees, records):
    answer = []

    dict = {}  # 차 번호: 누적 주차 시간
    temp = {}  # 차 번호: 입차 시간
    for i in records:
        x = i.split()
        if x[2] == "IN":
            if x[1] not in dict:
                dict[x[1]] = 0
            temp[x[1]] = x[0]  # 입차 시간
        else:  # 시간 계산
            outtime = list(map(int, x[0].split(":")))
            intime = list(map(int, temp[x[1]].split(":")))
            del temp[x[1]]
            time = (outtime[0] - intime[0]) * 60 + (outtime[1] - intime[1])
            dict[x[1]] += time

    for key, value in temp.items():  # 23:59분 출차
        intime = list(map(int, value.split(":")))
        outtime = [23, 59]
        time = (outtime[0] - intime[0]) * 60 + (outtime[1] - intime[1])
        dict[key] += time

    for key, value in dict.items():
        result = fees[1]  # 기본 요금
        if value - fees[0] > 0:  # 기본 요금 초과시
            if (value - fees[0]) % fees[2] != 0:
                result += (((value - fees[0]) // fees[2]) + 1) * fees[3]
            else:
                result += ((value - fees[0]) // fees[2]) * fees[3]
        dict[key] = result  # 차 번호: 주차 요금

    dict = sorted(dict.items())  # 차량 번호가 작은 자동차부터

    for i in dict:  # list
        answer.append(i[1])

    return answer