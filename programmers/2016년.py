def solution(a, b):
    list = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]

    month = a - 1
    day = b - 1

    monthday = 0
    if (month == 1):
        monthday += 31
    elif (month == 2):
        monthday += 60
    elif (month == 3):
        monthday += 91
    elif (month == 4):
        monthday += 121
    elif (month == 5):
        monthday += 152
    elif (month == 6):
        monthday += 182
    elif (month == 7):
        monthday += 213
    elif (month == 8):
        monthday += 244
    elif (month == 9):
        monthday += 274
    elif (month == 10):
        monthday += 305
    elif (month == 11):
        monthday += 335

    temp = monthday + day

    index = temp % 7

    answer = list[index]
    return answer