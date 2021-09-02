def solution(s):
    answer = []

    s = s[1:len(s) - 1]  # 큰따옴표 제거

    result = []
    val = ''
    for j in range(len(s)):
        i = s[j]
        if i == '{':
            temp = []
        elif i.isdigit():  # 숫자이면
            val += i
        elif i == ',' and len(val) != 0:  # 괄호 안의 쉼표이면
            temp.append(val)
            val = ''
        elif i == '}':
            if len(val) != 0:  # 마지막 숫자가 남아있으면
                temp.append(val)
                val = ''
            result.append(temp)

    result.sort(key=lambda x: len(x))  # 길이 순으로 정렬

    # 반복문_값이 answer에 없으면 추가
    for i in result:
        for j in i:
            if int(j) not in answer:
                answer.append(int(j))
    return answer