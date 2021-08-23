from itertools import permutations

def solution(n):
    num = list(n)

    # 소수 구하기
    x = [True] * 9999999
    line = int(9999999 * 0.5)
    for i in range(2, line + 1):
        if x[i] == True:
            for j in range(2, 9999999):
                if i * j < 9999999:
                    x[i * j] = False
                else:
                    break

    cnt = 0
    perlist = []

    for i in num:  # 1자리 수
        perlist.append(int(i))

    # 2자리수 부터 순열로 구함
    for i in range(2, len(num) + 1):
        temp = list(permutations(num, i))
        for j in temp:
            a = int(''.join(j))
            perlist.append(a)

    # set을 활용하여 중복 제거
    for j in set(perlist):
        if x[j] == True:  # 소수이면_0과 1은 소수 x
            if j == 0:
                pass
            elif j == 1:
                pass
            else:
                cnt += 1

    return cnt