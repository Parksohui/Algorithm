def solution(progresses, speeds):
    answer = []

    temp = []
    for i in range(len(progresses)):
        x = 100 - progresses[i]
        a = x % speeds[i]
        if (a != 0):  # 나머지 있으면 몫+1 추가
            temp.append(x // speeds[i] + 1)
        else:  # 나머지 없으면 몫 추가
            temp.append(x // speeds[i])

    k = 0
    for i in range(len(temp)):
        count = 0
        if (k != i):
            continue
        else:
            answer.append(count)
        for j in range(i, len(temp)):
            if (temp[j] <= temp[i]):  # 값이 작으면 같이 배포 가능
                answer[-1] += 1
            else:  # 크면 같이 배포 불가능
                k = j
                break

    return answer