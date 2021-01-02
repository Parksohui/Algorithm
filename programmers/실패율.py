def solution(N, stages):
    answer = []

    temp = [0] * N

    count = len(stages)  # 1단계는 전부 시도중이므로 처음은 전체 인원
    j = 0
    for i in temp:
        x = stages.count(j + 1)
        if (x == 0 or count == 0):  # 0으로 나누기 방지
            temp[j] = 0
        else:
            temp[j] = x / count
        j += 1
        count -= x  # 앞단계 클리어하지 못한 사람 빼기

    while (temp.count(-1) != len(temp)):  # 내림차순으로 스테이지 정렬
        answer.append(temp.index(max(temp)) + 1)
        temp[temp.index(max(temp))] = -1

    return answer