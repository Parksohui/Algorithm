def solution(table, languages, preference):
    answer = ''

    arr = []
    result = {}
    for i in range(len(table)): #list, dict
        arr.append(list(table[i].split()))
        result[arr[i][0]] = 0

    for i in range(len(languages)): #선호도 계산
        for j in range(len(arr)):
            if languages[i] in arr[j]:
                x = arr[j].index(languages[i])
                result[arr[j][0]] += preference[i] * (6 - x)

    #정렬_총합이 가장 높은 직업군 return
    result = sorted(result.items(), key=lambda item: (-item[1], item[0]))
    answer = result[0][0]

    return answer