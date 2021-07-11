def number(temp):
    if temp == 'zero':
        return '0'
    elif temp == 'one':
        return '1'
    elif temp == 'two':
        return '2'
    elif temp == 'three':
        return '3'
    elif temp == 'four':
        return '4'
    elif temp == 'five':
        return '5'
    elif temp == 'six':
        return '6'
    elif temp == 'seven':
        return '7'
    elif temp == 'eight':
        return '8'
    elif temp == 'nine':
        return '9'
    else:
        return '-1'


def solution(s):
    answer = ''

    temp = ''
    for i in range(len(s)):
        if s[i].isdigit():
            temp = ''
            answer += s[i]
        else:
            temp += s[i]
            if i == len(s) - 1:
                answer += number(temp)
            elif s[i + 1].isdigit():
                answer += number(temp)
            elif len(temp) >= 3:
                x = number(temp)
                if x == '-1':
                    pass
                else:
                    answer += x
                    temp = ''

    return int(answer)