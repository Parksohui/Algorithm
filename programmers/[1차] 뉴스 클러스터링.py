import math


def solution(str1, str2):
    answer = 0

    A = []
    B = []
    x = []
    minus = []

    # str1, str2 두 글자씩 끊어서 list
    for i in range(len(str1) - 1):
        if (str1[i].isalpha() and str1[i + 1].isalpha()):
            A.append(str1[i].lower() + "" + str1[i + 1].lower())
    for i in range(len(str2) - 1):
        if (str2[i].isalpha() and str2[i + 1].isalpha()):
            B.append(str2[i].lower() + "" + str2[i + 1].lower())
            x.append(str2[i].lower() + "" + str2[i + 1].lower())

    for i in A:  # 교집합
        if (i in x):
            minus.append(i)
            x.pop(x.index(i))

    sumlist = []

    for i in A:  # 합집합
        sumlist.append(i)
        if (i in B):
            B.pop(B.index(i))
    sumlist = sumlist + B

    if (len(minus) == 0 and len(sumlist) == 0):  # 모두 공집합일 경우
        answer = 1
    else:  # 공집합이 아닐 경우
        answer = len(minus) / len(sumlist)
    answer = math.trunc(answer * 65536)  # 버림

    return answer