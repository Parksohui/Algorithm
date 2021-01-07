def solution(people, limit):
    answer = 0
    index1 = 0  # 처음
    index2 = len(people) - 1  # 끝

    people.sort()
    while True:
        if (people[index1] + people[index2] <= limit):  # 최대와 최소 합이 limit보다 작으면 태울수 있음
            index1 += 1  # index 증가(앞에서 접근)
        index2 -= 1  # index 감소 (뒤에서 접근)
        answer += 1  # 보트 개수
        if (index1 > index2):  # 리스트 다 순회 완료
            break
        if (index1 == index2):  # 리스트 값 하나 남음
            answer += 1
            break

    return answer