def solution(skill, skill_trees):
    answer = 0

    for i in skill_trees:
        count = 0
        temp = []
        for j in range(len(i)):  # 값 하나씩 읽어서
            for k in range(len(skill)):
                if (skill[k] == i[j]):  # skill에 있는 글자가 i에 들어있다면
                    temp.append(skill[k])  # list에 추가
        if (len(temp) == 0):  # list 길이가 0이면 -> skill에 상관없음
            answer += 1
        for j in range(len(temp)):
            if (skill[j] == temp[j]):  # list와 skill을 비교
                count += 1
            if (count == len(temp)):  # list길이와 같다면 선행 스킬 순서 skill에 맞다는 의미
                answer += 1

    return answer