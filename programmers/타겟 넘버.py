def solution(numbers, target):
    answer = 0

    root = [0]  # 처음 0부터 시작

    for i in numbers:  # numbers에서 숫자를 받아와 root값에 더해주고 빼주는 경우의 수
        temp = []
        for j in root:
            temp.append(j + i)
            temp.append(j - i)
            root = temp  # temp값을 root로 만들어줌

    answer = temp.count(target)  # 최종 결과 값에서 원하는 target 값이 몇개 있는지 확인

    return answer