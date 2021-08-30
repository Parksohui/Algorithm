def solution(price, money, count):
    answer = -1

    want = 0
    for i in range(1, count + 1): #놀이기구 이용료 계산
        want += price * i

    answer = want - money #모자란 돈
    if answer <= 0: #모자란 돈이 없으면
        answer = 0

    return answer