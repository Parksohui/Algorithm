# 두 수의 곱= (최대 공약수) * (최소 공배수)

def gcd(a, b):  # 최대공약수
    while (b != 0):
        r = a % b
        a = b
        b = r
        if (b == 1):
            return 1
    return a


def lcm(a, b):  # 최소공배수
    return a * b / gcd(a, b)


def solution(arr):
    answer = 0

    answer = arr.pop()
    while (len(arr) != 0):
        x = arr.pop()  # list 값 pop
        answer = lcm(answer, x)  # 두 수의 최소공배수와 list의 값의 최소 공배수를 구함

    return answer