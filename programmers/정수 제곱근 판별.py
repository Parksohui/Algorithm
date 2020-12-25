import math

def solution(n):
    answer = 0
    answer = int(math.sqrt(n))

    if answer * answer != n:  # 제곱근이 아니면
        answer = -1
    else:
        answer = answer + 1
        answer = answer * answer
    return answer