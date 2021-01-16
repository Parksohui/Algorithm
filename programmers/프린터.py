def solution(priorities, location):
    temp = []

    for i in range(len(priorities)):  # index 저장
        temp.append(i)

    result = []
    while (len(priorities) != 0):
        if (len(priorities) == 1):  # 길이가 1이면 바로 출력 가능
            result.append(temp[0])  # index 저장
            break
        templist = priorities[1:]
        x = priorities[0]
        y = temp[0]
        priorities = templist
        temp = temp[1:]
        if (x < max(priorities)):  # 대기목록에 중요도 높은 문서가 한개라도 있다면
            priorities.append(x)  # 가장 마지막에 넣음
            temp.append(y)  # index도 가장 마지막으로 넣음
        else:  # 대기목록에 중요도 높은 문서가 없으면
            result.append(y)  # result list에 추가

    return result.index(location) + 1  # index의 위치를 결과로 반환