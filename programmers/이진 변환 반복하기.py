def solution(s):
    answer = []

    zero = 0
    turn = 0

    while (s != "1"):
        zero += s.count("0")  # 0의 개수 count
        temp = s.count("1")
        s = format(temp, 'b')  # 1의 개수를 이진 변환
        turn += 1

    answer.append(turn)
    answer.append(zero)
    
    return answer