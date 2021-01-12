def solution(n, words):
    answer = []

    temp = words[0][-1]  # 첫번째 단어의 끝 문자

    for i in range(1, len(words)):
        forward = words[i][0]  # 다음 단어의 첫 문자
        tempwords = words[0:i + 1]  # 중복 확인을 위해 list에 저장
        if (tempwords.count(words[i]) > 1):  # 중복이 있다면
            answer.append(i % n + 1)  # 번호
            answer.append(i // n + 1)  # 차례
            break
        if (forward != temp):  # 첫 문자와 끝 문자가 같지 않다면
            answer.append(i % n + 1)  # 번호
            answer.append(i // n + 1)  # 차례
            break
        temp = words[i][-1]  # 끝 문자를 현재 단어의 끝 문자로 바꿔줌

    if (len(answer) == 0):  # list의 길이가 0이면 탈락자 없음
        answer.append(0)
        answer.append(0)
    return answer