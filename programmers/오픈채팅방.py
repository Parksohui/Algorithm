def solution(record):
    answer = []

    iduser = dict()

    for i in range(len(record)):
        temp = record[i].split()
        if (temp[0] == "Enter" or temp[0] == "Change"):  # Enter, Change이면 유저아이디와 닉네임 추가
            iduser[temp[1]] = temp[2]

    for i in range(len(record)):
        temp = record[i].split()
        if (temp[0] == "Enter"):
            answer.append(iduser[temp[1]] + "님이 들어왔습니다.")
        elif (temp[0] == "Leave"):
            answer.append(iduser[temp[1]] + "님이 나갔습니다.")

    return answer