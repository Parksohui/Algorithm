def solution(cacheSize, cities):
    answer = 0

    result = []

    for i in range(len(cities)):
        cities[i] = cities[i].lower()  # 대문자, 소문자 상관 x
        if (cacheSize == 0):  # cacheSize가 0이면 다 실행 시간 5
            answer = len(cities) * 5
            break
        if (cities[i] in result):  # 값이 있으면
            result.pop(result.index(cities[i]))
            result.append(cities[i])  # 맨 끝으로
            answer += 1  # 1
        else:
            if (len(result) == cacheSize):  # 캐시 크기만큼 다 채워져있으면
                result.pop(0)  # 제일 안쓰는 것 pop
            answer += 5  # 5
            result.append(cities[i])

    return answer