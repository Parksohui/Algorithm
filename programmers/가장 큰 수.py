def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))  # 문자열로 바꿔줌
    numbers.sort(key=lambda x: x * 4, reverse=True)  # 각 문자열을 4번 반복시켜서 비교

    answer = ''.join(numbers)  # 이어붙이기

    # 문자열이 다 0이면 answer은 0
    if answer.count("0") == len(answer):
        answer = "0"

    return answer