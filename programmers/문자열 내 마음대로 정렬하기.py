def solution(strings, n):
    answer = []

    temp = []
    for i in range(len(strings)):  # n번째 글자 리스트에 추가
        temp.append(strings[i][n])
    temp.sort()

    for i in range(len(temp)):
        same = []
        if (i != 0 and temp[i - 1] == temp[i]):  # 앞에서 이미 추가한 문자라면
            continue
        count = temp.count(temp[i])  # 같은 문자 count
        for j in range(len(temp)):
            if (count > 1):  # 같은 문자가 여러개면
                if (strings[j][n] == temp[i]):  # 새로운 리스트에 추가
                    same.append(strings[j])
            else:  # 같은 문자가 없다면
                if (strings[j][n] == temp[i]):  # 바로 결과 리스트에 추가
                    answer.append(strings[j])
        if (len(same) != 0):  # 리스트에 값이 있다면
            same.sort()
            for k in same:
                answer.append(k)

    return answer